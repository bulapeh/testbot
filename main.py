import telebot
import random
from config_test import token, week_schedule, barsik_pictures, ekz_pictures

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def greeting(message):
    bot.send_message(
        message.from_user.id,
        'Что тебя интересует?',
        reply_markup=navigation_keyboard(),
    )

    bot.register_next_step_handler(message, switcher)


@bot.message_handler(content_types=['text'])
def error(message):
    switcher(message)
    rofl_switcher(message)
    subject_switcher(message)


@bot.callback_query_handler(func=lambda call: True)
def schedule_switcher(call):
    if call.data in week_schedule.keys():
        bot.send_photo(call.from_user.id, photo=week_schedule[call.data])
    elif call.data in ekz_pictures.keys():
        bot.send_photo(call.from_user.id, photo=ekz_pictures[call.data])


def schedule_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn_monday = telebot.types.InlineKeyboardButton(
        'Понедельник', callback_data='monday'
    )
    btn_tuesday = telebot.types.InlineKeyboardButton(
        'Вторник', callback_data='tuesday'
    )
    btn_wednesday = telebot.types.InlineKeyboardButton(
        'Среда', callback_data='wednesday'
    )
    btn_thursday = telebot.types.InlineKeyboardButton(
        'Четверг', callback_data='thursday'
    )
    btn_friday = telebot.types.InlineKeyboardButton(
        'Пятница', callback_data='friday'
    )
    btn_saturday = telebot.types.InlineKeyboardButton(
        'Суббота', callback_data='saturday'
    )
    return keyboard.add(
        btn_monday, btn_tuesday, btn_wednesday,
        btn_thursday, btn_friday, btn_saturday
    )


def schedule(message):
    bot.send_message(
        message.from_user.id,
        'Выбери день недели:',
        reply_markup=schedule_keyboard()
    )


# -------------------------------------------------------------------------------


def subject_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_philosophy = telebot.types.KeyboardButton('Философия')
    btn_management = telebot.types.KeyboardButton('Менеджмент')
    return keyboard.add(btn_philosophy, btn_management)


def material_philosophy_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn_philosophy_manual = telebot.types.InlineKeyboardButton(
        'Методичка по философии',
        url='https://1drv.ms/w/s!Ahvuy7A_scK2kXo-ebaKKKN07jxl?e=oFDVe7'
    )
    return keyboard.add(btn_philosophy_manual)


def material_management_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn_management_manual = telebot.types.InlineKeyboardButton(
        'Методичка по менеджменту',
        url='https://cloud.mail.ru/public/ufDN/Sog2KuEtf'
    )
    return keyboard.add(btn_management_manual)


def subject_choice(message):
    bot.send_message(
        message.from_user.id,
        'Выбери нужный предмет:',
        reply_markup=subject_keyboard()
    )


def subject_switcher(message):
    if message.text.lower() == 'философия':
        material_philosophy_choice(message)
    elif message.text.lower() == 'менеджмент':
        material_management_choice(message)


def material_philosophy_choice(message):
    bot.send_message(
        message.from_user.id,
        'Выбери нужный материал:',
        reply_markup=material_philosophy_keyboard()
    )


def material_management_choice(message):
    bot.send_message(
        message.from_user.id,
        'Выбери нужный материал:',
        reply_markup=material_management_keyboard()
    )


# -------------------------------------------------------------------------------
def rofl_switcher(message):
    if message.text.lower() == 'какой ты барсик сегодня?':
        barsik(message)
    elif message.text.lower() == 'аудиоирония':
        audio(message)


def audio_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn_wednesday = telebot.types.InlineKeyboardButton(
        'Венсдей', callback_data='wednesday_girl'
    )
    return keyboard.add(btn_wednesday)


def audio(message):
    bot.send_message(
        message.from_user.id,
        'Какой звук тебя интересует?',
        reply_markup=audio_keyboard(),
    )


def barsik(message):
    bot.send_message(message.from_user.id, 'Сегодня ты...')
    barsik_random_picture(message)


def rofl(message):
    bot.send_message(
        message.from_user.id,
        'Что тебя интересует?',
        reply_markup=rofl_keyboard()
    )


def barsik_random_picture(message):
    lst = list(barsik_pictures.keys())
    random_key = random.randint(0, 15)
    random_word = lst[random_key]
    bot.send_photo(
        message.from_user.id,
        photo=barsik_pictures[random_word],
        caption=random_word
    )


def rofl_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_barsik = telebot.types.KeyboardButton('Какой ты барсик сегодня?')
    btn_audio = telebot.types.KeyboardButton('Аудиоирония')
    return keyboard.add(btn_barsik, btn_audio)


# -------------------------------------------------------------------------------


def switcher(message):
    if message.text.lower() == 'расписание':
        schedule(message)
    elif message.text.lower() == 'материалы':
        subject_choice(message)
    elif message.text.lower() == 'развлечения':
        rofl(message)
    elif message.text.lower() == 'экзамены':
        ekz(message)


def ekz(message):
    bot.send_message(
        message.from_user.id,
        'Какая группа тебе нужна?',
        reply_markup=ekz_keyboard()
    )


def navigation_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_schedule = telebot.types.KeyboardButton('Расписание')
    btn_entertainment = telebot.types.KeyboardButton('Развлечения')
    btn_materials = telebot.types.KeyboardButton('Материалы')
    btn_ekz = telebot.types.KeyboardButton('Экзамены')
    return keyboard.add(btn_schedule, btn_materials, btn_entertainment, btn_ekz)


def ekz_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn_23b = telebot.types.InlineKeyboardButton('ИТЕ-23б', callback_data='23b')
    btn_all = telebot.types.InlineKeyboardButton('Все группы', callback_data='all_groups')
    return keyboard.add(btn_all, btn_23b)


bot.infinity_polling()
