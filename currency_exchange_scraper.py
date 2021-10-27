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
def handler_text(message):
    text = message.text

    try:
        date = datetime.datetime.strftime(datetime.datetime.strptime(text, '%Y-%m-%d'), '%Y-%m-%d')
        result = collect_exchange_rates(date)
        if len(result) == 0:
            bot.send_message(message.chat.id, "NBU provides currency exchange rate only in working dates. \n"
                                              "You tried to find exchange rates for day for which rates do not exist.\n "
                                              "There is no exchange rates for the day. \n"
                                              "Please, choose other day.")
            return

    except ValueError:
        bot.send_message(message.chat.id, "Incorrect data format, should be YYYY-MM-DD. \n"
                                          "Please, try again!")
        return

    bot.send_message(message.chat.id, "Please, choose the following exchange rate:", reply_markup=gen_markup(result))


def gen_markup(result):
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(
        InlineKeyboardButton("UAH/USD", callback_data=result['USD']),
        InlineKeyboardButton("UAH/EUR", callback_data=result['EUR']),
        InlineKeyboardButton("UAH/PLN", callback_data=result['PLN'])
    )
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    print(call.data)
    bot.send_message(call.message.chat.id, call.data)


def collect_exchange_rates(date):  # The data easy to collect using National Bank`s API, but I created scraper to exercise.

    scraped_data = []
    url = f'https://bank.gov.ua/en/markets/exchangerates?date={date}&period=daily'
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    for item in soup.select('tbody tr td'):
        scraped_data.append(item.text)

    abbreviations = scraped_data[1::5]
    currency_quantity = scraped_data[2::5]
    row_exchange_rate = scraped_data[4::5]
    exchange_rates = []

    for quantity, rate in zip(currency_quantity, row_exchange_rate):
        _result = round(float(rate)/float(quantity), 2)
        exchange_rates.append(_result)

    data_for_bot = {}

    for abbreviation, exchange_rate in zip(abbreviations, exchange_rates):
        data_for_bot[abbreviation] = exchange_rate
    return data_for_bot


bot.polling()