import openai
import config
import os

openai.api_key = os.getenv('Open_AI_Token')

def gpt_response(message):
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
    return response['choices'][0]['text']