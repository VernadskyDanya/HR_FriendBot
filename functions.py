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
    bot.send_message(message_chat_id, 'По согласованию с руководителем отпуск можно перенести или отменить в'
                                      ' личном кабинете SAP:\n'
                                      '<b>Портал - Услуги и сервисы - Корпоративные сервисы '
                                      'самообслуживания - SAP портал - Управление отпусками - Перенос отпуска</b>\n'
                                      'Если у вас возникли сложности, вы всегда можете обраться по адресу '
                                      '<b>"Фронт-офис ЦКР Почтамтская"</b>', parse_mode = 'HTML')
def Spravka(message_chat_id,bot,types):
    pass
def Bolnichnyi(message_chat_id,bot,types):
    pass
def Komandirovka(message_chat_id,bot,types):
    pass