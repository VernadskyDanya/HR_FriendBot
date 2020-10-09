import telebot
import passwords
from telebot import types
bot = telebot.TeleBot(passwords.key)

commands = {  # command description used in the "help" command
    'help '        : 'Информация о существующих командах',
    'start '       : 'Знакомство с ботом'
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, " + str(message.from_user.first_name)
                     + ", это твой личный HR друг! Я всегда готов помочь тебе с вопросами")
    button1 = types.InlineKeyboardButton(text = "1. ☕", callback_data = "1")
    button2 = types.InlineKeyboardButton(text = "2. ❓", callback_data = "2")
    button3 = types.InlineKeyboardButton(text = "3. 🕵️‍♂️ ", callback_data = "3")
    button4 = types.InlineKeyboardButton(text = "4. 📈 ", callback_data = "4")
    button5 = types.InlineKeyboardButton(text = "5. 📴 ", callback_data = "5")
    button6 = types.InlineKeyboardButton(text = "6. 📛", callback_data = "6")
    markup = types.InlineKeyboardMarkup()
    markup.add(button1,button2,button3,button4,button5,button6)
    bot.send_message(message.chat.id, "Чем тебе помочь?\n"
                                      "1. Хочу выпить кофе с коллегой ☕\n"
                                      "2. У меня вопрос по кадровому администрированию ❓\n"
                                      "3. Хочу учиться/развиваться 🕵️‍♂️ \n"
                                      "4. Хочу расти и/или перемещаться в компании 📈 \n"
                                      "5. У меня вопрос по административной или ИТ поддержке 📴 \n"
                                      "6. Я не нашел ответа на свой вопрос 📛\n"
                     , reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        options = {
            '1': "Coffee",
            '2': "Personnel administration",
            '3': "Study",
            '4': "Grow",
            '5': "IT",
            '6': "Not found",
        }

        if options.get(call.data) =="Coffee":
            button1 = types.InlineKeyboardButton(text="Бот Hot Coffee ☕ ",
                                                 url = "https://t.me/GPN_S_coffee_bot")
            markup = types.InlineKeyboardMarkup()
            markup.add(button1)
            bot.send_message(message.chat.id, "Для этого перейди в другой чат бот" ,reply_markup=markup)

        if options.get(call.data) =="Personnel administration":
            button1 = types.InlineKeyboardButton(text="Я оформлен в КЦ", callback_data="1")
            button2 = types.InlineKeyboardButton(text="Я оформлен в ГПН-С", callback_data="2")
            markup = types.InlineKeyboardMarkup()
            markup.add(button1,button2)
            bot.send_message(message.chat.id, 'Выбери отдел:', reply_markup=markup)

        if options.get(call.data) == "Study":
            button1 = types.InlineKeyboardButton(text="1", callback_data="1")
            button2 = types.InlineKeyboardButton(text="2", callback_data="2")
            button3 = types.InlineKeyboardButton(text="3", callback_data="3")
            button4 = types.InlineKeyboardButton(text="4", callback_data="4")
            markup = types.InlineKeyboardMarkup()
            markup.add(button1, button2, button3, button4)
            bot.send_message(message.chat.id, '1. Какие возможности для обучения есть в компании?\n'
                                              '2. Я самостоятельно выбрал курс - что дальше?\n'
                                              '3. Хочу учить других!\n'
                                              '4. Как понять, чему мне поучиться?\n', reply_markup=markup)

bot.polling(none_stop=False, interval=0, timeout=20)