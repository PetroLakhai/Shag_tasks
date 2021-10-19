
import requests
import telebot

BOT_TOKEN = '2032664074:AAHgJDJOBGpa_zkZiKgO-Napp099xRiQ1fY'
PRIVAT_BANK_API_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

response = requests.get(PRIVAT_BANK_API_URL).json()[0]
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands='start')
def handle(message):
    buy = round(float(response["buy"]), 2)
    sale = round(float(response["sale"]), 2)
    bot.send_message(message.chat.id, f'The bot help you to calculate how many Ukrainian Hryvnia do you need to buy '
                                      f'certain number of American Dollars or how many Ukrainian Hryvnia you receive '
                                      f'when you sell certain number of American Dollars. '
                                      f'According to current exchange rate published on Privat Bank website.\n'
                                      f'\n'
                                      f'The exchange rate for American Dollar (USD) for today is: {buy}/{sale}.\n'
                                      f'\n'
                                      f'Please, write "buy" or "sale".')


@bot.message_handler(content_types=['text'])
def handler_text(message):
    text = message.text
    if text == "buy":
        msg_text = 'Enter the sum of purchase'
        type_operation = 'sale'
    elif text == "sale":
        msg_text = 'Enter the sum of sale'
        type_operation = 'buy'
    msg = bot.send_message(message.chat.id, msg_text)  # noqa
    bot.register_next_step_handler(msg, exchange, type_operation=type_operation) # noqa


def exchange(message, **kwargs):
    type_operation = kwargs.get('type_operation')
    value = float(message.text)
    total_money = float(response[type_operation]) * value
    message_to_send = f'You need {total_money} UAH' if type_operation == 'sale' else f'You will get {total_money} UAH.'

    bot.send_message(message.chat.id, message_to_send)


bot.polling()
