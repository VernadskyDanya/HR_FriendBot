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
    button2 = types.InlineKeyboardButton(text="❔ Задать новый вопрос", callback_data="start")
    markup = types.InlineKeyboardMarkup()
    markup.add(button1, button2)
    bot.send_message(message_chat_id, "Для этого нажми кнопку Hot Coffee", reply_markup=markup)


def pers_adm(message_chat_id, bot, types):
    button1 = types.InlineKeyboardButton(text="в КЦ", callback_data="KS")
    button2 = types.InlineKeyboardButton(text="в ГПН-С", callback_data="GPN-S")
    markup = types.InlineKeyboardMarkup()
    markup.add(button1, button2)
    button3 = types.InlineKeyboardButton(text="Назад", callback_data="start")
    markup.row(button3)
    bot_message = bot.send_message(message_chat_id, 'Я оформлен:', reply_markup= markup)
    return bot_message


def KSorGPN_S(message_chat_id, bot, types, KSorGPN_Sbool):
    if not KSorGPN_Sbool:
        button1 = types.InlineKeyboardButton(text="Как перенести/отменить отпуск?", callback_data="perenosKS")
        button2 = types.InlineKeyboardButton(text="Как заказать справку (2НДФЛ, о месте работы и др.)?", callback_data="spravkaKS")
        button3 = types.InlineKeyboardButton(text="Как передать больничный в кадры?", callback_data="bolnichnyiKS")
        button4 = types.InlineKeyboardButton(text="Как оформить командировку?", callback_data="komandirovkaKS")
    else:
        button1 = types.InlineKeyboardButton(text="Как перенести/отменить отпуск?", callback_data="perenosGPN_S")
        button2 = types.InlineKeyboardButton(text="Как заказать справку (2НДФЛ, о месте работы и др.)?", callback_data="spravkaGPN_S")
        button3 = types.InlineKeyboardButton(text="Как передать больничный в кадры?", callback_data="bolnichnyiGPN_S")
        button4 = types.InlineKeyboardButton(text="Как оформить командировку?", callback_data="komandirovkaGPN_S")
    button5 = types.InlineKeyboardButton(text="Назад", callback_data="personnel administration")
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, "Выбери вопрос:", reply_markup=markup)


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
    button1 = types.InlineKeyboardButton(text="Какие возможности для обучения есть в компании?", callback_data="Kakie vozm")
    button2 = types.InlineKeyboardButton(text="Я самостоятельно выбрал курс - что дальше?", callback_data="Samost")
    button3 = types.InlineKeyboardButton(text="Хочу учить других!", callback_data="Wanttoteach")
    button4 = types.InlineKeyboardButton(text="Как понять, чему мне поучиться?", callback_data ="Kakponyat")
    button5 = types.InlineKeyboardButton(text="Назад", callback_data="start")
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, 'Выбери вопрос:', reply_markup=markup)

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
    bot.send_message(message_chat_id, 'В компании активно работает <b>кафедра Закупок</b>. '
                                      'Для того, чтобы присоединиться '
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
    button1 = types.InlineKeyboardButton(text="Где увидеть вакансии компании?", callback_data="Vakansii")
    button2 = types.InlineKeyboardButton(text="Какие правила внутреннего перехода?", callback_data="VnytrPerehod")
    button3 = types.InlineKeyboardButton(text="Что необходимо сделать, чтобы перейти на другую роль "
                                              "или в смежное направление?", callback_data="OtherRol")
    button4 = types.InlineKeyboardButton(text="Как выстроить индивидуальный план развития?", callback_data ="IndividPlan")
    button5 = types.InlineKeyboardButton(text="Назад", callback_data="start")
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    markup.row(button5)
    bot.send_message(message_chat_id, 'Выбери вопрос:', reply_markup=markup)


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

def individ_plan(message_chat_id, bot, types):
    button1 = types.InlineKeyboardButton(text="Где заполнить план развития?", callback_data="GdePlan")
    button2 = types.InlineKeyboardButton(text="Как заполнить план развития?", callback_data="KakPlan")
    button3 = types.InlineKeyboardButton(text="Помощь в составлении плана развития", callback_data="HelpPlan")
    button4 = types.InlineKeyboardButton(text="Назад", callback_data="grow")
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    bot_message = bot.send_message(message_chat_id, 'Выбери вопрос:', reply_markup=markup)
    return bot_message

def gde_plan(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Для создания Индивидуального плана развития (ИПР) на '
                                      'корпоративном портале есть инструмент: <b>База знаний - '
                                      'Портал обучения - Карьерный портал - Мое развитие - Мой план развития</b>\n'
                                      'После заполнения ИПР его согласовывает Руководитель',
                                      parse_mode='HTML', reply_markup= menu_button(types))

def kak_plan(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Для того, чтобы заполнить план развития максимально качественно, '
                                      'рекомендуем вам: обратиться за обратной связью от руководителя, '
                                      'определить свои сильные и слабые строны, <b>сфокусироваться на 2-3 '
                                      'компетенциях в год</b>\n'
                                      'В компании действет принцип 70-20-10, который говорит о том, что\n'
                                      '<b>70%</b> - это обучение в ходе деятельности'
                                      '<b>20%</b> - социальное обучение, включающее '
                                      'наставничество и общение с опытными экспертами\n'
                                      '<b>10%</b> - формальное обучение (тренинги и обучающие '
                                      'программы Корпоративного университета и внешних провайдеров)',                                       parse_mode='HTML', reply_markup= menu_button(types))

def help_plan(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Если вам нужна помощь или консультация в составлении ИПР, '
                                      'пожалуйста, обратитесь к своему HR - партнеру. Данный '
                                      'запрос останется конфиденциальным',
                                      parse_mode='HTML', reply_markup= menu_button(types))

""" 
Раздел "У меня вопрос по административной или ИТ поддержке" 
"""


def it(message_chat_id,bot,types):
    button1 = types.InlineKeyboardButton(text="Как заказать разовый пропуск посетителю?", callback_data="RazProp")
    button2 = types.InlineKeyboardButton(text="Как заказать временный пропуск?", callback_data="VremProp")
    button3 = types.InlineKeyboardButton(text="Как отправить документы в другой офис?", callback_data="DocOffice")
    button4 = types.InlineKeyboardButton(text="У меня вопрос по ИТ - куда обратиться?", callback_data="questIT")
    button5 = types.InlineKeyboardButton(text="Как заказать канцелярию?", callback_data ="Kanzel")
    button6 = types.InlineKeyboardButton(text="У меня другой вопрос", callback_data="OthQuest")
    button7 = types.InlineKeyboardButton(text="Назад", callback_data="start")
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    markup.row(button4)
    markup.row(button5)
    markup.row(button6)
    markup.row(button7)
    bot.send_message(message_chat_id, 'Выбери вопрос:', reply_markup=markup)


def raz_prop(message_chat_id, bot, types):
    button1 = types.InlineKeyboardButton(text="Посетитель внешний (из другой компании, "
                                              "физическое лицо)", callback_data="VneshPos")
    button2 = types.InlineKeyboardButton(text="Посетитель из другого ДО", callback_data="VnytrPos")
    button3 = types.InlineKeyboardButton(text="Назад", callback_data="IT")
    markup = types.InlineKeyboardMarkup()
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    bot_message = bot.send_message(message_chat_id, 'Выбери категорию:', reply_markup=markup)
    #return bot_message


def vnesh_pos(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'В период COVID у посетителя должен быть на руках свежий (не более 7 дней) '
                                      'отрицательный тест. Заявку на пропуск необходимо согласовать с Барминым М.В.\n'
                                      'Также вы можете попросить помочь помощника вашего подразделения',
                                      parse_mode='HTML', reply_markup= menu_button(types))


def vnytr_pos(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'У посетителя должен быть "зеленый" статус в градуснике. '
                                      'Заявку на пропуск необходимо согласовать с Барминым М.В.\n'
                                      'Также вы можете попросить помочь помощника вашего подразделения',
                                      parse_mode='HTML', reply_markup= menu_button(types))


def vrem_prop(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Необходимо оформленную по форме заявку направить на согласование Бармину М.В. '
                                      'Вход в офис возможет только при наличии приложения Градусник '
                                      'и "зеленого" статуса в нем',
                                      parse_mode='HTML', reply_markup= menu_button(types))


def doc_office(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Через ячейку "Исходящая почта" на 1 этаже, с указанием адреса и получателя',
                                      parse_mode='HTML', reply_markup= menu_button(types))


def quest_it(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'По всем вопросам вы можете '
                                      'позвонить или написать на 8888 (телефон и адрес почты совпадает)',
                                      parse_mode='HTML', reply_markup= menu_button(types))


def kanzel(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Заявка на канцелярию формируется помощником подразделения. '
                                      'Если вам нужны какие-то определенные вещи, сообщите помощнику.',
                                      parse_mode='HTML', reply_markup= menu_button(types))

def oth_quest(message_chat_id, bot, types):
    bot.send_message(message_chat_id, 'Пожалуйста, обратитесь к помощнику своего подразделения',
                                      parse_mode='HTML', reply_markup= menu_button(types))


def not_found(message_chat_id, bot, types):
    button4 = types.InlineKeyboardButton(text="Назад", callback_data="grow")
    bot.send_message(message_chat_id, 'Пожалуйста, обратитесь к своему HR-партнеру',
                                      parse_mode='HTML', reply_markup= menu_button(types))