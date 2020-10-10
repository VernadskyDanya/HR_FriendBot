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