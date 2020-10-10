"""Модуль, где хранятся кнопки и рекакции на них"""

#кнопка для возврата к основным вопросам
def Menu_button(types):
    button = types.InlineKeyboardButton(text="❔ Задать новый вопрос", callback_data="Start")
    markup = types.InlineKeyboardMarkup()
    markup.add(button)
    return markup

def Coffee(message_chat_id, bot, types):
    button1 = types.InlineKeyboardButton(text="Бот Hot Coffee ☕ ",
                                         url="https://t.me/GPN_S_coffee_bot")
    markup = types.InlineKeyboardMarkup()
    markup.add(button1)
    bot.send_message(message_chat_id, "Для этого создан другой чат бот", reply_markup=markup)

def Pers_adm(message_chat_id, bot, types):
    button1 = types.InlineKeyboardButton(text="Я оформлен в КЦ", callback_data="KS")
    button2 = types.InlineKeyboardButton(text="Я оформлен в ГПН-С", callback_data="GPN-S")
    markup = types.InlineKeyboardMarkup()
    markup.add(button1, button2)
    bot.send_message(message_chat_id, 'Выбери отдел:', reply_markup=markup)

def KS(message_chat_id, bot, types):
    button1 = types.InlineKeyboardButton(text="1. ", callback_data="Perenos")
    button2 = types.InlineKeyboardButton(text="2. ", callback_data="Spravka")
    button3 = types.InlineKeyboardButton(text="3. ", callback_data="Bolnichnyi")
    button4 = types.InlineKeyboardButton(text="4. ", callback_data="Komandirovka")
    markup = types.InlineKeyboardMarkup()
    markup.add(button1, button2, button3, button4)
    bot.send_message(message_chat_id, "1. Как перенести/отменить отпуск?\n"
                                      "2. Как заказать справку (2НДФЛ, о месте работы и др.)?\n"
                                      "3. Как передать больничный в кадры?\n"
                                      "4. Как оформить командировку?\n", reply_markup=markup)

def Study(message_chat_id,bot,types):
    button1 = types.InlineKeyboardButton(text="1", callback_data="1")
    button2 = types.InlineKeyboardButton(text="2", callback_data="2")
    button3 = types.InlineKeyboardButton(text="3", callback_data="3")
    button4 = types.InlineKeyboardButton(text="4", callback_data="4")
    markup = types.InlineKeyboardMarkup()
    markup.add(button1, button2, button3, button4)
    bot.send_message(message_chat_id, '1. Какие возможности для обучения есть в компании?\n'
                                      '2. Я самостоятельно выбрал курс - что дальше?\n'
                                      '3. Хочу учить других!\n'
                                      '4. Как понять, чему мне поучиться?\n', reply_markup=markup)

def Perenos(message_chat_id,bot,types):
    bot.send_message(message_chat_id, 'По согласованию с руководителем отпуск можно перенести или отменить в '
                                      'личном кабинете SAP:\n'
                                      '<b>Портал - Услуги и сервисы - Корпоративные сервисы '
                                      'самообслуживания - SAP портал - Управление отпусками - Перенос отпуска</b>\n'
                                      'Если у вас возникли сложности, вы всегда можете обраться по адресу '
                                      '<b>"Фронт-офис ЦКР Почтамтская"</b>', parse_mode = 'HTML',
                                      reply_markup= Menu_button(types))
def Spravka(message_chat_id,bot,types):
    bot.send_message(message_chat_id, 'Спавки можно заказать в личном кабинете SAP: <b>Портал - Услуги и сервисы - '
                                      'Корпоративные сервисы самообслуживания - SAP портал - Заказ справок</b>\n'
                                      'Также справку можно заказать по внтреннему номеру <b>8181</b>,'
                                      ' или по внешнему - <b>8 800 350 8181</b>', parse_mode='HTML',
                                      reply_markup= Menu_button(types))
def Bolnichnyi(message_chat_id,bot,types):
    bot.send_message(message_chat_id, 'Через ячейку на 1-м этаже "Исходящая документация" - на '
                                      'Почтамтскую 3-5, во Фронт-офис ЦКР', parse_mode='HTML',
                                      reply_markup= Menu_button(types))
def Komandirovka(message_chat_id,bot,types):
    bot.send_message(message_chat_id, 'Командировку можно оформить в личном кабинете SAP Портала: '
                                      '<b>Услуги и сервисы - Корпоративные сервисы самообслуживания - '
                                      'SAP портал - Командировки</b>', parse_mode='HTML',
                                      reply_markup= Menu_button(types))