import telebot
import passwords
from telebot import types
bot = telebot.TeleBot(passwords.key)

commands = {  # command description used in the "help" command
    'help ': 'Информация о существующих командах',
    'start ': 'Знакомство с ботом'
}

bot.delete_webhook()
"""
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
"""


def start(message_chat_id):
    button1 = types.InlineKeyboardButton(text="☕ Хочу выпить кофе с коллегой", callback_data="coffee")
    button2 = types.InlineKeyboardButton(text="📖 У меня вопрос по HR", callback_data="HRquestion")
    button3 = types.InlineKeyboardButton(text="📴  Вопрос по админ. или ИТ поддержке", callback_data="IT")
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    bot.send_message(message_chat_id, "Чем тебе помочь?\n", reply_markup=markup)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    bot.send_message(message.chat.id, "Привет, " + str(message.from_user.first_name)
                     + ", это твой личный HR друг! Я всегда готов помочь тебе с вопросами.\n"
                       "Ты всегда можешь вернуться в меню командой /start")
    start(message.chat.id)


bot_message = 0  # Переменная для удаления предыдущих сообщений

import functions as func

FUNCTIONS = dict(coffee=func.coffee, HRquestion=func.hr_question, personnel_administration=func.pers_adm,
                 study=func.study, perenosKS=func.perenosKS, spravkaKS=func.spravkaKS,
                 bolnichnyiKS=func.bolnichnyiKS, komandirovkaKS=func.komandirovkaKS,
                 perenosGPN_S=func.perenosGPN_S, spravkaGPN_S=func.spravkaGPN_S,
                 bolnichnyiGPN_S=func.bolnichnyiGPN_S, komandirovkaGPN_S=func.komandirovkaGPN_S,
                 Kakie_vozm=func.vozmoznosti, Samost=func.samost, Wanttoteach=func.wanttoteach,
                 Kakponyat=func.kakponyat, grow=func.grow, Vakansii=func.vakansii, VnytrPerehod=func.vnytr_perehod,
                 OtherRol=func.other_rol, IndividPlan=func.individ_plan, IT=func.it, RazProp=func.raz_prop,
                 VneshPos=func.vnesh_pos, VnytrPos=func.vnytr_pos, VremProp=func.vrem_prop, DocOffice=func.doc_office,
                 questIT=func.quest_it, Kanzel=func.kanzel, OthQuest=func.oth_quest, not_found=func.not_found,
                 )


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global bot_message
    if call.data == "start":
        start(call.message.chat.id)
    elif call.data == "KS":
        if (bot_message):
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
        bot_message = 0
        from functions import KSorGPN_S
        KSorGPN_S(call.message.chat.id, bot, types, False)
    elif call.data == "GPN-S":
        if bot_message:
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
        bot_message = 0
        from functions import KSorGPN_S
        KSorGPN_S(call.message.chat.id, bot, types, True)
    elif (call.data) == "GdePlan":
        if (bot_message):
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
        bot_message = 0
        from functions import gde_plan
        gde_plan(call.message.chat.id, bot, types)
    elif (call.data) == "KakPlan":
        if (bot_message):
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
        bot_message = 0
        from functions import kak_plan
        kak_plan(call.message.chat.id, bot, types)
    elif (call.data) == "HelpPlan":
        if (bot_message):
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
        bot_message = 0
        from functions import help_plan
        help_plan(call.message.chat.id, bot, types)
    else:
        FUNCTIONS[call.data](call.message.chat.id, bot, types)


bot.polling(none_stop=False, interval=0, timeout=20)
"""
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://hr-friendtb.herokuapp.com/' + passwords.key)
    return "!", 200


server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
"""
