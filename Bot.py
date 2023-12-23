import telebot
from telebot import types


TOKEN = '6540302676:AAHr2m6er2wf1VDiMW8pQEJf6_1fLRzz_n0'

bot = telebot.TeleBot(TOKEN)

# Словарь с данными пользователей
user_data = {}


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {'name': '', 'age': '', 'phone': ''}
    send_welcome(message)


def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Перезапуск")
    item2 = types.KeyboardButton("Регистрация")
    item3 = types.KeyboardButton("Мои данные")
    item4 = types.KeyboardButton("Диаграммы")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, f"Здравствуйте {message.from_user.first_name}!\n\nЗдесь вы можете записаться, чтобы принять участие в проекте или предложить свой. Выберите регистрацию или напишите /register. После регистрации с вами свяжется один из наших сотрудников.\n"
                                      "\nТакже вы можете посмотреть актуальную информацию по проектам, для этого выберите диаграммы или напишите /diagrams'", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Перезапуск")
def restart(message):
    user_id = message.from_user.id
    user_data[user_id] = {'name': '', 'age': '', 'phone': ''}
    send_welcome(message)


@bot.message_handler(func=lambda message: message.text == "Регистрация" or message.text == "/register")
def registration(message):
    bot.send_message(message.chat.id, "Введите ваше ФИО:")
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    user_id = message.from_user.id
    user_data[user_id]['name'] = message.text
    bot.send_message(message.chat.id, "Введите ваш возраст:")
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    try:
        age = int(message.text)
        user_id = message.from_user.id
        user_data[user_id]['age'] = age
        bot.send_message(message.chat.id, "Введите ваш номер телефона:")
        bot.register_next_step_handler(message, get_phone)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректный возраст (целое число):")
        bot.register_next_step_handler(message, get_age)


def get_phone(message):
    user_id = message.from_user.id
    user_data[user_id]['phone'] = message.text
    bot.send_message(message.chat.id, "Регистрация завершена. Ваши данные:")
    show_data(message)


@bot.message_handler(func=lambda message: message.text == "Мои данные")
def show_data(message):
    user_id = message.from_user.id
    data = user_data[user_id]
    if all(data.values()):
        response = f"Имя: {data['name']}\nВозраст: {data['age']}\nТелефон: {data['phone']}"
    else:
        response = "Вы не завершили регистрацию. Пожалуйста, введите все данные."
    bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda message: message.text == "Диаграммы" or message.text == "/diagrams")
def diagrams(message):
    markup = types.InlineKeyboardMarkup(row_width=4)
    item1 = types.InlineKeyboardButton("Диаграмма 1", callback_data='1')
    item2 = types.InlineKeyboardButton("Диаграмма 2", callback_data='2')
    item3 = types.InlineKeyboardButton("Диаграмма 3", callback_data='3')
    item4 = types.InlineKeyboardButton("Диаграмма 4", callback_data='4')
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Выберите диаграмму:", reply_markup=markup)
