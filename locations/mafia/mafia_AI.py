import os
import openai
import config


openai.api_key = os.getenv('Open_AI_Token')


def prompt(text):
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=0.5,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
    return response['choices'][0]['text']

