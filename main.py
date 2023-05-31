import os
import telebot
import openai
from telebot import types
import config
from locations.mafia import mafia
from locations.gpt_chat import gpt_response
from locations import menu



location = {}

openai.api_key = os.getenv('Open_AI_Token')
bot = telebot.TeleBot(os.getenv('Telegram_Token'))

@bot.message_handler(commands=['start', 'menu'])
def hello(message):
    global location
    location[message.chat.id] = 'menu'
    menu.start(message)

@bot.message_handler(commands = ['info'])
def info(message):
    global location
    menu.menu_info(message, location[message.chat.id])


@bot.message_handler(func = lambda message: True)
def gpt_chat(message):
    global location
    if message.text == 'Назад':
        location[message.chat.id] = 'menu'
        menu.start(message)
        return
    
    elif message.text == 'GPT-3':
        location[message.chat.id] = 'friend_chat'
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        btn1 = types.KeyboardButton(text="Назад")
        keyboard.add(btn1)
        bot.send_message(message.chat.id, '<b>Chat-GPT</b> слушает:', parse_mode = 'html', reply_markup = keyboard)
        return
    
    elif message.text == 'Мафия':
        location[message.chat.id] = 'mafia'
        #btn1 = types.KeyboardButton(text="Назад")
        #keyboard.add(btn1)
        bot.send_message(message.chat.id, 'Игра в мафию:', parse_mode = 'html')
        mafia.game_loop(message.chat.id)
        return
    
    elif location[message.chat.id] == 'friend_chat': 
        bot_message = bot.send_message(message.chat.id, '<b>Chat-GPT</b> is responding...', parse_mode = 'html')
        ans = gpt_response(message)
        bot.edit_message_text(ans,message.chat.id, bot_message.message_id)

    else:
        bot.send_message(message.chat.id, 'Извини, я не знаю, что ответить')

    


bot.polling(none_stop = True)