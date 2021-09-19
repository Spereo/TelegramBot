import telebot
from telebot import types
import datetime

bot = telebot.TeleBot("1247121725:AAFECNrqKn4HrwSCGKaYqx3E-7i5Vt4WplU")

smile1 = "📖"
smile2 = "👤"

lessons = [
f"\r\n\r\n1 пара (9:10 - 10:40)\r\n{smile1} МДК.04.02 Процессы приготовления, подготовки к реализации горячих и холодных сладких блюд, десертов, напитков\r\n{smile2} Шлыкова Е.Д.\r\n\r\n2 пара (10:50 - 12:20)\r\n{smile1} МДК.04.02 Процессы приготовления, подготовки к реализации горячих и холодных сладких блюд, десертов, напитков\r\n{smile2} Шлыкова Е.Д.\r\n\r\n3 пара (12:40 - 14:10)\r\n{smile1} ОП.07 Иностранный язык в профессиональной деятельности/ОП.12 Этика и психология профессиональной деятельности\r\n{smile2} Муравьева А.Д./Дударец В.В\r\n\r\n4 пара (14:30 - 16:00)\r\n{smile1} ОУД 16. Индивидуальный учебный проект\r\n{smile2} Алдошина Н.А.",
f"\r\n\r\n1 пара (9:10 - 10:40)\r\n{smile1} ОП.05 Основы калькуляции и учета\r\n{smile2} Доброева И.Н.\r\n\r\n2 пара (10:50 - 12:20)\r\n{smile1} ОП.04 Экономические и правовые основы профессиональной деятельности\r\n\r\n3 пара (12:40 - 14:10)\r\n{smile1} ОП.11  Организация обслуживания в ресторане\r\n{smile2} Сорокина А.А.",
f"\r\n\r\n1 пара (9:10 - 10:40)\r\n{smile1} МДК.04.02 Процессы приготовления, подготовки к реализации горячих и холодных сладких блюд, десертов, напитков\\ МДК.04.01 Организация приготовления,  подготовки к реализации горячих и холодных сладких блюд, десертов, напитков\r\n{smile2} Шлыкова Е.Д.\r\n\r\n2 пара (10:50 - 12:20)\r\n{smile1} МДК.04.02 Процессы приготовления, подготовки к реализации горячих и холодных сладких блюд, десертов, напитков\r\n{smile2} Шлыкова Е.Д.\r\n\r\n3 пара (12:40 - 14:10)\r\n{smile1} ОП.09 Физическая культура\r\n{smile2} Мельнов А.А.\r\n\r\n4 пара (14:30 - 16:00)\r\n{smile1} ОП.13 Основы предпринимательской деятельности\r\n{smile2} Алдошина Н.А.",
f"\r\n\r\n1 пара (9:10 - 10:40)\r\n{smile1} ОП.04 Экономические и правовые основы профессиональной деятельности\r\n\r\n2 пара (10:50 - 12:20)\r\n{smile1} ОП.12 Этика и психология профессиональной деятельности\r\n{smile2} Дударец В.В\r\n\r\n3 пара (12:40 - 14:10)\r\n{smile1}ОП.11  Организация обслуживания в ресторане\\ ОП.04 Экономические и правовые основы профессиональной деятельности\r\n{smile2} Сорокина А.А.\\2 нед",
f"\r\n\r\n1 пара (9:10 - 10:40)\r\n{smile1} МДК.04.01 Организация приготовления,  подготовки к реализации горячих и холодных сладких блюд, десертов, напитков\r\n{smile2} Шлыкова Е.Д.\r\n\r\n2 пара (10:50 - 12:20)\r\n{smile1} ОУД 16. Индивидуальный учебный проект\r\n{smile2} Алдошина Н.А.\r\n\r\n3 пара (12:40 - 14:10)\r\n{smile1} ОП.07 Иностранный язык в профессиональной деятельности\r\n{smile2} Муравьева А.Д."
]

days = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница"
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Сегодня')
    item2 = types.KeyboardButton('Завтра')
    item3 = types.KeyboardButton('Расписание')
    markup.row(item1, item2)
    markup.row(item3)
    bot.send_message(message.chat.id, "Привееет!\r\nЯ - твой помощник, который будет подсказывать расписание занятий. Не стесняйся писать мне, когда не знаешь, на какую пару идти 💜", reply_markup=markup)


@bot.message_handler(content_types= ['text'])
def answer(message):
    msg = message.text
    today = datetime.datetime.today()

    if msg == 'Сегодня':
        numberOfDay = datetime.datetime.today().weekday()
        if numberOfDay > 4:
            bot.send_message(message.chat.id, "Сегодня пар нет, наслаждайся выходным 💜")
        else:
            if today.month < 10:
                todayMonth = "0" + f"{today.month}"
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(today.day, todayMonth, today.year) + lessons[numberOfDay])
            else:
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(today.day, today.month, today.year) + lessons[numberOfDay])

    if msg == 'Завтра':
        numberOfDay = datetime.datetime.today().weekday() + 1
        if numberOfDay == 7:
            numberOfDay = 0
        if numberOfDay > 4:
            bot.send_message(message.chat.id, "Завтра пар нет, наслаждайся выходным 💜")
        else:
            tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
            if today.month < 10:
                tomorrowMonth = "0" + f"{tomorrow.month}"
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(tomorrow.day, tomorrowMonth, tomorrow.year) + lessons[numberOfDay])
            else:
                bot.send_message(message.chat.id, days[numberOfDay] + ", " + "{}.{}.{}".format(tomorrow.day, tomorrow.month, tomorrow.year) + lessons[numberOfDay])

    if msg == 'Расписание':
        markup = types.InlineKeyboardMarkup()
        item_0 = types.InlineKeyboardButton(text='Пн', callback_data='0')
        item_1 = types.InlineKeyboardButton(text='Вт', callback_data='1')
        item_2 = types.InlineKeyboardButton(text='Ср', callback_data='2')
        item_3 = types.InlineKeyboardButton(text='Чт', callback_data='3')
        item_4 = types.InlineKeyboardButton(text='Пт', callback_data='4')
        markup.add(item_0, item_1, item_2, item_3, item_4)
        bot.send_message(message.chat.id, "Выбери день недели 💜", reply_markup=markup)

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    markup = types.InlineKeyboardMarkup()
    item_0 = types.InlineKeyboardButton(text='Пн', callback_data='0')
    item_1 = types.InlineKeyboardButton(text='Вт', callback_data='1')
    item_2 = types.InlineKeyboardButton(text='Ср', callback_data='2')
    item_3 = types.InlineKeyboardButton(text='Чт', callback_data='3')
    item_4 = types.InlineKeyboardButton(text='Пт', callback_data='4')
    markup.add(item_0, item_1, item_2, item_3, item_4)
    call_index = int(call.data)
    editText = days[call_index] + lessons[call_index]
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=editText, reply_markup=markup)

bot.polling(none_stop=True)
