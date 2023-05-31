import os
import random
import config
import telebot
#from mafia_AI import prompt
import openai


bot = telebot.TeleBot(os.getenv('Telegram_Token'))
openai.api_key = os.getenv('Open_AI_Token')


def prompt(text):
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
    return response['choices'][0]['text']


def game_loop(user):
    history = ''
    std_prompt = 'привет, мы играем в мафию, есть 3 роли - мирный житель, комиссар и мафия, днем все обсуждают кого они считают мафией, а ночью сначала мафия может убить одного игрока, затем комиссар может проверить одного игрока и узнать его роль. цель мирных жителей - понять, кто является мафией, задача мафии - убить всех мирных.'
    roles = ['мирный житель', 'мирный житель', 'мирный житель', 'комиссар', 'мафия']
    random.shuffle(roles)
    players = {'Оливия': roles[0], 'Александр': roles[1], 'Наталья': roles[2], 'Джордж': roles[3], 'Роберт': roles[4]}
    bot.send_message(user, players)
    bot.send_message(user, 'Ведущий: Игра в мафию начинается, игроки, представтесь.')
    olivia_prompt = std_prompt + f" Тебя зовут Оливия, ты - {players['Оливия']}, тебе нельзя говорить про свою роль, отвечай только за своего персонажа, других игроков зовут Александр, Наталья, Джордж и Роберт, представься другим игрокам, расскажи о своих увлечениях. Оливия:"
    ans = 'Оливия: ' + prompt(olivia_prompt)
    history += ans
    bot.send_message(user, ans)

    alex_prompt = std_prompt + history + f" Тебя зовут Александр, ты - {players['Александр']}, тебе нельзя говорить про свою роль, отвечай только за своего персонажа, других игроков зовут Оливия, Наталья, Джордж и Роберт, представься другим игрокам, расскажи о своих увлечениях. Александр:"
    ans = 'Александр: ' + prompt(alex_prompt)
    history += ans
    bot.send_message(user, ans)

    
    natalya_prompt = std_prompt + history + f" Тебя зовут Наталья, ты - {players['Наталья']}, тебе нельзя говорить про свою роль,отвечай только за своего персонажа, других игроков зовут Александр, Оливия, Джордж и Роберт, представься другим игрокам, расскажи о своих увлечениях. Наталья:"
    ans = 'Наталья: ' + prompt(natalya_prompt)
    history += ans
    bot.send_message(user, ans)

    george_prompt = std_prompt + history + f" Тебя зовут Джордж, ты - {players['Джордж']}, тебе нельзя говорить про свою роль,отвечай только за своего персонажа, других игроков зовут Александр, Оливия, Наталья и Роберт, представься другим игрокам, расскажи о своих увлечениях. Джордж:"
    ans = 'Джордж: ' + prompt(george_prompt)
    history += ans
    bot.send_message(user, ans)

    robert_prompt = std_prompt + history + f" Тебя зовут Роберт, ты - {players['Роберт']}, тебе нельзя говорить про свою роль,отвечай только за своего персонажа, других игроков зовут Александр, Оливия, Джордж и Наталья, представься другим игрокам, расскажи о своих увлечениях. Роберт:"
    ans = 'Роберт: ' + prompt(robert_prompt)
    history += ans
    bot.send_message(user, ans)
    