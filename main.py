import telebot
import passwords
from telebot import types
bot = telebot.TeleBot(passwords.key)

commands = {  # command description used in the "help" command
    'help '        : 'Информация о существующих командах',
    'start '       : 'Знакомство с ботом'
}
first_welcome = False


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global first_welcome
    if (not first_welcome):
        bot.send_message(message.chat.id, "Привет, " + str(message.from_user.first_name)
                     + ", это твой личный HR друг! Я всегда готов помочь тебе с вопросами")
        first_welcome = True
    button1 = types.InlineKeyboardButton(text = "Хочу выпить кофе с коллегой ☕", callback_data = "coffee")
    button2 = types.InlineKeyboardButton(text = "У меня вопрос по кадровому администрированию ❓", callback_data = "personnel administration")
    button3 = types.InlineKeyboardButton(text = "Хочу учиться/развиваться 🕵️‍♂️ ", callback_data = "study")
    button4 = types.InlineKeyboardButton(text = "Хочу расти и/или перемещаться в компании 📈 ", callback_data = "grow")
    button5 = types.InlineKeyboardButton(text = "У меня вопрос по административной или ИТ поддержке 📴 ", callback_data = "IT")
    button6 = types.InlineKeyboardButton(text = "Я не нашел ответа на свой вопрос 📛", callback_data = "not found")
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    markup.row(button5)
    markup.row(button6)
    bot.send_message(message.chat.id, "Чем тебе помочь?\n", reply_markup=markup)

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

        if (call.data) == "Kakie vozm":
            from functions import vozmoznosti
            vozmoznosti(message.chat.id, bot, types)

        if (call.data) == "Samost":
            from functions import samost
            samost(message.chat.id, bot, types)

        if (call.data) == "Wanttoteach":
            from functions import wanttoteach
            wanttoteach(message.chat.id, bot, types)

        if (call.data) == "Kakponyat":
            from functions import kakponyat
            kakponyat(message.chat.id, bot, types)

        if call.data == "grow":
            from functions import grow
            bot_message = grow(message.chat.id, bot, types)

        if (call.data) == "Vakansii":
            from functions import vakansii
            vakansii(message.chat.id, bot, types)

        if (call.data) == "VnytrPerehod":
            from functions import vnytr_perehod
            vnytr_perehod(message.chat.id, bot, types)

        if (call.data) == "OtherRol":
            from functions import grow
            grow(message.chat.id, bot, types)

        if (call.data) == "IndividPlan":
            from functions import individ_plan
            bot_message
            bot_message = individ_plan(message.chat.id, bot, types)

        if (call.data) == "GdePlan":
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
            from functions import gde_plan
            gde_plan(message.chat.id, bot, types)

        if (call.data) == "KakPlan":
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
            from functions import kak_plan
            kak_plan(message.chat.id, bot, types)

        if (call.data) == "HelpPlan":
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
            from functions import help_plan
            help_plan(message.chat.id, bot, types)

bot.polling(none_stop=False, interval=0, timeout=20)