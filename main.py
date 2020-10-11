import telebot
import passwords
from telebot import types
bot = telebot.TeleBot(passwords.key)

commands = {  # command description used in the "help" command
    'help '        : 'Информация о существующих командах',
    'start '       : 'Знакомство с ботом'
}

import os
from flask import Flask, request
import logging
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
server = Flask(__name__)
os.environ['FLASK_ENV'] = 'development'

@server.route('/' + passwords.key, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, " + str(message.from_user.first_name)
                     + ", это твой личный HR друг! Я всегда готов помочь тебе с вопросами")
    button1 = types.InlineKeyboardButton(text = "1. ☕", callback_data = "coffee")
    button2 = types.InlineKeyboardButton(text = "2. ❓", callback_data = "personnel administration")
    button3 = types.InlineKeyboardButton(text = "3. 🕵️‍♂️ ", callback_data = "study")
    button4 = types.InlineKeyboardButton(text = "4. 📈 ", callback_data = "grow")
    button5 = types.InlineKeyboardButton(text = "5. 📴 ", callback_data = "IT")
    button6 = types.InlineKeyboardButton(text = "6. 📛", callback_data = "not found")
    markup = types.InlineKeyboardMarkup()
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_message(message.chat.id, "Чем тебе помочь?\n"
                                      "1. Хочу выпить кофе с коллегой ☕\n"
                                      "2. У меня вопрос по кадровому администрированию ❓\n"
                                      "3. Хочу учиться/развиваться 🕵️‍♂️ \n"
                                      "4. Хочу расти и/или перемещаться в компании 📈 \n"
                                      "5. У меня вопрос по административной или ИТ поддержке 📴 \n"
                                      "6. Я не нашел ответа на свой вопрос 📛\n", reply_markup=markup)

    bot_message = 5  # Переменная для удаления предыдущих сообщений

    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if call.data == "start":
            send_welcome(message)

        if call.data =="coffee":
            from functions import coffee
            coffee(message.chat.id, bot, types)

        if call.data =="personnel administration":
            from functions import pers_adm
            nonlocal bot_message
            bot_message = pers_adm(message.chat.id, bot, types)

        if call.data == "KS":
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
            from functions import KSorGPN_S
            KSorGPN_S(message.chat.id, bot, types, False)

        if call.data == "study":
            from functions import study
            study(message.chat.id, bot, types)

        if call.data == "perenosKS":
            from functions import perenosKS
            perenosKS(message.chat.id, bot, types)

        if call.data == "spravkaKS":
            from functions import spravkaKS
            spravkaKS(message.chat.id, bot, types)

        if call.data == "bolnichnyiKS":
            from functions import bolnichnyiKS
            bolnichnyiKS(message.chat.id, bot, types)

        if call.data == "komandirovkaKS":
            from functions import komandirovkaKS
            komandirovkaKS(message.chat.id, bot, types)

        if call.data == "GPN-S":
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
            from functions import KSorGPN_S
            KSorGPN_S(message.chat.id, bot, types, True)

        if call.data == "perenosGPN_S":
            from functions import perenosGPN_S
            perenosGPN_S(message.chat.id, bot, types)

        if (call.data) == "spravkaGPN_S":
            from functions import komandirovkaGPN_S
            komandirovkaGPN_S(message.chat.id, bot, types)

        if (call.data) == "bolnichnyiGPN_S":
            from functions import komandirovkaGPN_S
            komandirovkaGPN_S(message.chat.id, bot, types)

        if (call.data) == "komandirovkaGPN_S":
            from functions import komandirovkaGPN_S
            komandirovkaGPN_S(message.chat.id, bot, types)

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://telegrambot151.herokuapp.com/' + passwords.key)
    return "!", 200


server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))