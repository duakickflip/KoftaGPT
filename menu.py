import telebot
import os
from telebot import types

bot = telebot.TeleBot(os.getenv('Telegram_Token'))

def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="GPT-3")
    btn2 = types.KeyboardButton(text="AI")
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Вы находитесь в меню \nНавигация по боту "/info"', reply_markup = keyboard)
    return

def menu_info(message, location):
    if location == 'menu':
        bot.send_message(message.chat.id, 'Добро пожаловать в телеграм-бота <b>KoftaGPT</b>', parse_mode='html')
    elif location == 'friend_chat':
        bot.send_message(message.chat.id, 'Чат-бот, работающий на технологии GPT-3')
    else:
        bot.send_message(message.chat.id, 'Локация не обнаружена \nКод ошибки: -1')