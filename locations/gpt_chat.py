import os
import openai
import config

openai.api_key = os.getenv('Open_AI_Token')

def gpt_response(message):
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt='You: ' + message + 'отвечай только за Friend, Friend: ',
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
    return response['choices'][0]['text']