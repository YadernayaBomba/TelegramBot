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