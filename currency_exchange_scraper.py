import datetime

import bs4
import environ
import requests
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

env = environ.Env()
environ.Env.read_env()  # reading .env file

BOT_TOKEN = env('TELEGRAM_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

DATE_FORMAT = '%Y-%m-%d'


@bot.message_handler(commands='start')
def handler(message):
    bot.send_message(message.chat.id, f'The bot can provide you exchange rates between\n'
                                      f'Ukrainian Hryvnia and American Dollar - UAH/USD,\n'
                                      f'Ukrainian Hryvnia and Euro - UAH/EUR,\n'
                                      f'Ukrainian Hryvnia and Polish Zloty - UAH/PLN\n'
                                      f'for all available date when Ukrainian National Bank provide the rates.\n'
                                      f'\n'
                                      f'You should write the date in YYYY-MM-DD format '
                                      f'on which you want to receive rates')


@bot.message_handler(content_types=['text'], func=lambda message: True)
def bot_message_handler(message):
    """
    Gets message from user, validates the data and creates dictionary for keyboard.
    """
    text = message.text
    chat_id = message.chat.id

    try:
        raw_date = datetime.datetime.strptime(text, DATE_FORMAT)
        date = datetime.datetime.strftime(raw_date, DATE_FORMAT)

    except ValueError:
        bot.send_message(chat_id, "Incorrect data format, should be YYYY-MM-DD. \n"
                                  "Please, try again!")
        return

    result = collect_exchange_rates(date)
    if not result:
        bot.send_message(chat_id, "NBU provides currency exchange rate only in working dates. \n"
                                  "You tried to find exchange rates for day for which rates do not exist.\n"
                                  "There is no exchange rates for the day. \n"
                                  "Please, choose other day.")

        return

    bot.send_message(
        chat_id, "Please, choose the following exchange rate:", reply_markup=generate_keyboard_markup(result)
    )


def generate_keyboard_markup(result):
    markup = InlineKeyboardMarkup()
    markup.row_width = 3  # Generates three buttons
    markup.add(
        InlineKeyboardButton("UAH/USD", callback_data=result['USD']),
        InlineKeyboardButton("UAH/EUR", callback_data=result['EUR']),
        InlineKeyboardButton("UAH/PLN", callback_data=result['PLN'])
    )
    return markup


@bot.callback_query_handler(func=lambda call: True)
def provide_exchange_rate(call):
    """
    Gets callback data from Telegram API and provides exchange rates from it.
    """
    bot.send_message(call.message.chat.id, call.data)


def collect_exchange_rates(date):
    """
    Gets date, scrapes exchange rates from NBU`s website and provides dictionary with them.
    """
    url = f'https://bank.gov.ua/en/markets/exchangerates?date={date}&period=daily'
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    scraped_data = [item.text for item in soup.select('tbody tr td')]

    abbreviations = scraped_data[1::5]
    currency_quantity = scraped_data[2::5]
    raw_exchange_rate = scraped_data[4::5]

    exchange_rates = [
        round(float(rate)/float(quantity), 2) for quantity, rate in zip(currency_quantity, raw_exchange_rate)
    ]

    data_for_bot = {abbreviation: exchange_rate for abbreviation, exchange_rate in zip(abbreviations, exchange_rates)}

    return data_for_bot


bot.polling()
