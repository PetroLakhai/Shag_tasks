
import requests
import bs4
import telebot
import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


BOT_TOKEN = '2063738701:AAFskS4MoeAsXbWWZCtLmL-CIoObdN3NkvU'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands='start')
def handler(message):
    bot.send_message(message.chat.id, f'Instruction of the bot')


@bot.message_handler(content_types=['text'], func=lambda message: True)
def handler_text(message):
    text = message.text

    try:
        date = datetime.datetime.strftime(datetime.datetime.strptime(text, '%Y-%m-%d'), '%Y-%m-%d')
        result = collect_exchange_rates(date)
        if len(result) == 0:
            bot.send_message(message.chat.id, "NBU provides currency exchange rate only in working dates. \n"
                                              "You tried incorrect date. There is no exchange rates for the day. \n"
                                              "Please, chose other day.")

    except ValueError:
        bot.send_message(message.chat.id, "Incorrect data format, should be YYYY-MM-DD. \n"
                                          "Please, try again!")
        return

    bot.send_message(message.chat.id, "Please, choose the following:", reply_markup=gen_markup())


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"), InlineKeyboardButton("No", callback_data="cb_no"))
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.send_message(call.message.chat.id, 'Answer is Yes')
    elif call.data == "cb_no":
        bot.send_message(call.message.chat.id, "Answer is No")


def collect_exchange_rates(date):  # The data easy to collect using National Bank`s API, but I created scraper to exercise.

    data = []
    url = f'https://bank.gov.ua/en/markets/exchangerates?date={date}&period=daily'
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    for item in soup.select('tbody tr td'):
        data.append(item.text)

    currency_name = []
    currency_row_name = data[3::5]

    for name in currency_row_name:
        currency_name.append(name[22:-20])

    abbreviations = data[1::5]
    currency_quantity = data[2::5]
    row_exchange_rate = data[4::5]
    exchange_rates = []

    for quantity, rate in zip(currency_quantity, row_exchange_rate):
        result = round(float(rate)/float(quantity), 3)
        exchange_rates.append(result)

    data_for_bot = {}

    for name, abbreviation, exchange_rate in zip(currency_name, abbreviations, exchange_rates):
        data_for_bot[f'{name} ({abbreviation})'] = exchange_rate
    print(data_for_bot)
    return data_for_bot


# bot.infinity_polling()
bot.polling()