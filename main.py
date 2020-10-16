import telebot
import passwords
from telebot import types
bot = telebot.TeleBot(passwords.key)

commands = {  # command description used in the "help" command
    'help '        : 'Информация о существующих командах',
    'start '       : 'Знакомство с ботом'
}

def start(message_chat_id):
    button1 = types.InlineKeyboardButton(text="☕ Хочу выпить кофе с коллегой", callback_data="coffee")
    button2 = types.InlineKeyboardButton(text="📖 У меня вопрос по HR", callback_data="HRquestion")
    button3 = types.InlineKeyboardButton(text="📴  Вопрос по админ. или ИТ поддержке", callback_data="IT")
    # button4 = types.InlineKeyboardButton(text = "📛 Я не нашел ответа на свой вопрос" , callback_data = "not found")
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

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "start":
        start(call.message.chat.id)

    if call.data =="coffee":
        from functions import coffee
        coffee(call.message.chat.id, bot, types)

    if call.data == "HRquestion":
        from functions import hr_question
        hr_question(call.message.chat.id, bot, types)

    if call.data =="personnel administration":
        from functions import pers_adm
        bot_message = pers_adm(call.message.chat.id, bot, types)

    if call.data == "KS":
        if (bot_message):
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
        bot_message = 0
        from functions import KSorGPN_S
        KSorGPN_S(call.message.chat.id, bot, types, False)

    if call.data == "study":
        from functions import study
        study(call.message.chat.id, bot, types)

    if call.data == "perenosKS":
        from functions import perenosKS
        perenosKS(call.message.chat.id, bot, types)

    if call.data == "spravkaKS":
        from functions import spravkaKS
        spravkaKS(call.message.chat.id, bot, types)

    if call.data == "bolnichnyiKS":
        from functions import bolnichnyiKS
        bolnichnyiKS(call.message.chat.id, bot, types)

    if call.data == "komandirovkaKS":
        from functions import komandirovkaKS
        komandirovkaKS(call.message.chat.id, bot, types)

    if call.data == "GPN-S":
        if bot_message:
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
        bot_message = 0
        from functions import KSorGPN_S
        KSorGPN_S(call.message.chat.id, bot, types, True)

    if call.data == "perenosGPN_S":
        from functions import perenosGPN_S
        perenosGPN_S(call.message.chat.id, bot, types)

    if (call.data) == "spravkaGPN_S":
        from functions import spravkaGPN_S
        spravkaGPN_S(call.message.chat.id, bot, types)

    if (call.data) == "bolnichnyiGPN_S":
        from functions import bolnichnyiGPN_S
        bolnichnyiGPN_S(call.message.chat.id, bot, types)

    if (call.data) == "komandirovkaGPN_S":
        from functions import komandirovkaGPN_S
        komandirovkaGPN_S(call.message.chat.id, bot, types)

    if (call.data) == "Kakie vozm":
        from functions import vozmoznosti
        vozmoznosti(call.message.chat.id, bot, types)

    if (call.data) == "Samost":
        from functions import samost
        samost(call.message.chat.id, bot, types)

    if (call.data) == "Wanttoteach":
        from functions import wanttoteach
        wanttoteach(call.message.chat.id, bot, types)

    if (call.data) == "Kakponyat":
        from functions import kakponyat
        kakponyat(call.message.chat.id, bot, types)

    if call.data == "grow":
        from functions import grow
        bot_message = grow(call.message.chat.id, bot, types)

    if (call.data) == "Vakansii":
        from functions import vakansii
        vakansii(call.message.chat.id, bot, types)

    if (call.data) == "VnytrPerehod":
        from functions import vnytr_perehod
        vnytr_perehod(call.message.chat.id, bot, types)

    if (call.data) == "OtherRol":
        from functions import other_rol
        other_rol(call.message.chat.id, bot, types)

    if (call.data) == "IndividPlan":
        from functions import individ_plan
        bot_message = individ_plan(call.message.chat.id, bot, types)

    if (call.data) == "GdePlan":
        if (bot_message):
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
        bot_message = 0
        from functions import gde_plan
        gde_plan(call.message.chat.id, bot, types)

    if (call.data) == "KakPlan":
        if (bot_message):
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
        bot_message = 0
        from functions import kak_plan
        kak_plan(call.message.chat.id, bot, types)

    if (call.data) == "HelpPlan":
        if (bot_message):
            bot.delete_message(bot_message.chat.id, bot_message.message_id)
        bot_message = 0
        from functions import help_plan
        help_plan(call.message.chat.id, bot, types)

    if call.data =="IT":
        from functions import it
        it(call.message.chat.id, bot, types)

    if call.data =="RazProp":
        from functions import raz_prop
        raz_prop(call.message.chat.id, bot, types)

    if call.data =="VneshPos":
        from functions import vnesh_pos
        vnesh_pos(call.message.chat.id, bot, types)

    if call.data =="VnytrPos":
        from functions import vnytr_pos
        vnytr_pos(call.message.chat.id, bot, types)

    if call.data =="VremProp":
        from functions import vrem_prop
        vrem_prop(call.message.chat.id, bot, types)

    if call.data =="DocOffice":
        from functions import doc_office
        doc_office(call.message.chat.id, bot, types)

    if call.data =="questIT":
        from functions import quest_it
        quest_it(call.message.chat.id, bot, types)

    if call.data =="Kanzel":
        from functions import kanzel
        kanzel(call.message.chat.id, bot, types)

    if call.data =="OthQuest":
        from functions import oth_quest
        oth_quest(call.message.chat.id, bot, types)

    if call.data =="not found":
        from functions import not_found
        not_found(call.message.chat.id, bot, types)

bot.polling(none_stop=False, interval=0, timeout=20)