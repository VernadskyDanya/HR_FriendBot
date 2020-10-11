"""Модуль, где хранятся кнопки и рекакции на них"""

#кнопка для возврата к основным вопросам
def menu_button(types):
    button = types.InlineKeyboardButton(text="❔ Задать новый вопрос", callback_data="start")
    markup = types.InlineKeyboardMarkup()
    markup.add(button)
    return markup


def coffee(message_chat_id, bot, types):
    button1 = types.InlineKeyboardButton(text="Бот Hot Coffee ☕ ",
                                         url="https://t.me/GPN_S_coffee_bot")
    markup = types.InlineKeyboardMarkup()
    markup.add(button1)
    bot.send_message(message_chat_id, "Для этого создан другой чат бот", reply_markup= menu_button(types))


def pers_adm(message_chat_id, bot, types):
    button1 = types.InlineKeyboardButton(text="Я оформлен в КЦ", callback_data="KS")
    button2 = types.InlineKeyboardButton(text="Я оформлен в ГПН-С", callback_data="GPN-S")
    markup = types.InlineKeyboardMarkup()
    markup.add(button1, button2)
    bot_message = bot.send_message(message_chat_id, 'Выбери отдел:', reply_markup= markup)
    return bot_message


def KSorGPN_S(message_chat_id, bot, types, KSorGPN_Sbool):
    if not KSorGPN_Sbool:
        button1 = types.InlineKeyboardButton(text="1.", callback_data="perenosKS")
        button2 = types.InlineKeyboardButton(text="2.", callback_data="spravkaKS")
        button3 = types.InlineKeyboardButton(text="3.", callback_data="bolnichnyiKS")
        button4 = types.InlineKeyboardButton(text="4.", callback_data="komandirovkaKS")
    else:
        button1 = types.InlineKeyboardButton(text="1.", callback_data="perenosGPN_S")
        button2 = types.InlineKeyboardButton(text="2.", callback_data="spravkaGPN_S")
        button3 = types.InlineKeyboardButton(text="3.", callback_data="bolnichnyiGPN_S")
        button4 = types.InlineKeyboardButton(text="4.", callback_data="komandirovkaGPN_S")
    markup = types.InlineKeyboardMarkup()
    markup.add(button1, button2, button3, button4)
    bot.send_message(message_chat_id, "1. Как перенести/отменить отпуск?\n"
                                      "2. Как заказать справку (2НДФЛ, о месте работы и др.)?\n"
                                      "3. Как передать больничный в кадры?\n"
                                      "4. Как оформить командировку?\n", reply_markup=markup)


def perenosKS(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'По согласованию с руководителем отпуск можно перенести или отменить в '
                                      'личном кабинете SAP:\n'
                                      '<b>Портал - Услуги и сервисы - Корпоративные сервисы '
                                      'самообслуживания - SAP портал - Управление отпусками - Перенос отпуска</b>\n'
                                      'Если у вас возникли сложности, вы всегда можете обраться по адресу '
                                      '<b>"Фронт-офис ЦКР Почтамтская"</b>', parse_mode = 'HTML',
                                      reply_markup= menu_button(types))
def spravkaKS(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Спавки можно заказать в личном кабинете SAP: <b>Портал - Услуги и сервисы - '
                                      'Корпоративные сервисы самообслуживания - SAP портал - Заказ справок</b>\n'
                                      'Также справку можно заказать по внтреннему номеру <b>8181</b>,'
                                      ' или по внешнему - <b>8 800 350 8181</b>', parse_mode='HTML',
                                      reply_markup= menu_button(types))
def bolnichnyiKS(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Через ячейку на 1-м этаже "Исходящая документация" - на '
                                      'Почтамтскую 3-5, во Фронт-офис ЦКР', parse_mode='HTML',
                                      reply_markup= menu_button(types))
def komandirovkaKS(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Командировку можно оформить в личном кабинете SAP Портала: '
                                      '<b>Услуги и сервисы - Корпоративные сервисы самообслуживания - '
                                      'SAP портал - Командировки</b>', parse_mode='HTML',
                                      reply_markup= menu_button(types))


"""
    Раздел "У меня вопрос по кадровому администрированию" -> "Я оформлен в ГПН-С" 
"""

def perenosGPN_S(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Вам необходимо <b>согласовать</b> перенос/отмену отпуска по почте с '
                                      '<b>линейным и функциональным руководителями</b>, и направить данное '
                                      'согласование кадровым администраторам ООО "Газпромнеть Снабжения"',
                                      parse_mode = 'HTML', reply_markup= menu_button(types))


def spravkaGPN_S(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Вам необходимо направить запрос на справку кадровым '
                                      'администраторам ООО "Газпромнеть Снабжения"', parse_mode='HTML',
                                      reply_markup= menu_button(types))


def bolnichnyiGPN_S(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Через ячейку на 1-м этаже "Исходящая документация" - на Малую Морскую, '
                                      '23 с указанием имени адресата', parse_mode='HTML',
                                      reply_markup= menu_button(types))


def komandirovkaGPN_S(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Узнать информацию можно в личном кабинете SAP Портала: <b>Услуги и сервисы - '
                                      'Корпоративные сервисы самообслуживания - Командировки: заявка и оформление</b>',
                                      parse_mode='HTML', reply_markup= menu_button(types))


"""
    Раздел "Хочу учиться/развиваться"
"""

def study(message_chat_id,bot,types):
    button1 = types.InlineKeyboardButton(text="1.", callback_data="Kakie vozm")
    button2 = types.InlineKeyboardButton(text="2.", callback_data="Samost")
    button3 = types.InlineKeyboardButton(text="3.", callback_data="Wanttoteach")
    button4 = types.InlineKeyboardButton(text="4.", callback_data ="Kakponyat")
    markup = types.InlineKeyboardMarkup()
    markup.add(button1, button2, button3, button4)
    bot.send_message(message_chat_id, '1. Какие возможности для обучения есть в компании?\n'
                                      '2. Я самостоятельно выбрал курс - что дальше?\n'
                                      '3. Хочу учить других!\n'
                                      '4. Как понять, чему мне поучиться?\n', reply_markup=markup)

def vozmoznosti(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Через портал компании (<b>База знаний - Портал обучения</b>) '
                                      'вы можете ознакомиться с многочисленными ресурсами компании.\n'
                                      'Например, в навигаторе образовательных продуктов вы можете подробнее '
                                      'ознакомиться с теми или иными тренингами, в каталоге обучения - '
                                      'выбрать интересный курс, или зайти в библиотеку для чтения литературы. '
                                      '<b>Важно, что многие курсы - бесплатны и доступны для самостоятельного '
                                      'назначения, пользуйтесь этой возможностью!</b> Если вы выбрали на '
                                      'Портале обучения или во внешних ресурсах платный курс, согласуйте '
                                      'необходимость и возможность данного обучения с руководителем и '
                                      'HR-партнером.\nВы также можете проконсультироваться с вашим HR-партнером"',
                                      parse_mode='HTML', reply_markup= menu_button(types))


def samost(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Согласуйте необходимость и возможность данного обучения '
                                      'с руководителем и HR-партнером подразделения',
                                      parse_mode='HTML', reply_markup= menu_button(types))


def wanttoteach(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'В компании активно работает <b>кафедра Закупок</b>. Для того, чтобы присоединиться '
                                      'к ней - сначала нужно определиться с тем, чему вы могли бы научить коллег. '
                                      'И далее обратиться к Екатерине Копылец',
                                      parse_mode='HTML', reply_markup= menu_button(types))


def kakponyat(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Рекомендуем вам определиться с <b>целями обучения</b>, запросить <b>обратную '
                                      'связь</b> от руководителя, а также провести <b>анализ своих сильных и слабых '
                                      'сторон в контексте выполняемых задач и проектов</b>. Если вам необходима '
                                      '<b>консультация</b>, вы можете обратиться к Татьяне Головиной',
                                      parse_mode='HTML', reply_markup= menu_button(types))


""" 
Раздел "Хочу расти и/или перемещаться в компании" 
"""

def grow(message_chat_id,bot,types):
    button1 = types.InlineKeyboardButton(text="1.", callback_data="Vakansii")
    button2 = types.InlineKeyboardButton(text="2.", callback_data="VnytrPerehod")
    button3 = types.InlineKeyboardButton(text="3.", callback_data="OtherRol")
    button4 = types.InlineKeyboardButton(text="4.", callback_data ="IndividPlan")
    markup = types.InlineKeyboardMarkup()
    markup.add(button1, button2, button3, button4)
    bot.send_message(message_chat_id, '1. Где увидеть вакансии компании?\n'
                                      '2. Какие правила внутреннего перехода?\n'
                                      '3. Что необходимо сделать, чтобы перейти на другую роль'
                                      ' или в смежное направление?\n'
                                      '4. Как выстроить индивидуальный план развития?\n', reply_markup=markup)


def vakansii(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Вакансии компании представлены на портале в разделе '
                                      '<b>Персонал - Вакансии.</b>\n'
                                      'Обязательно ознакомьтесь с <b>правилами внутреннего перехода</b> '
                                      'перед тем, как откливаться на позицию',
                                      parse_mode='HTML', reply_markup= menu_button(types))

def vnytr_perehod(message_chat_id, bot, types):
    bot.send_message(message_chat_id, '<b>Рассмотрение вакансий</b> в рамках группы компании возможно по согласованию '
                                      'с руководителем. В случае вашего перехода, вы также должны согласовать '
                                      'дату перехода с руководителем. При этом руководитель имеет право попросить '
                                      'вас задержаться для завершения задач <b>на срок до 2 месяцев</b>',
                                      parse_mode='HTML', reply_markup= menu_button(types))

def other_rol(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Есть несколько важных аспектов для перехода:\n'
                                      '- заявите о себе, повысьте свою "видимость", заполнив профиль на '
                                      '<b>Карьерном портале</b>: База знаний - Портал обучения - '
                                      'Карьерный портал- определите направление развития и сформируйте '
                                      '<b>индивидуальный план развития</b>',
                                      parse_mode='HTML', reply_markup= menu_button(types))