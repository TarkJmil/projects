# المكتبات الضرورية
import openai
from dotenv import load_dotenv
import os
import requests

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


stablediffusion_api_key=os.getenv('DREAMSTUDIO_KEY')

ENGINE_ID='stable-diffusion-xl-1024-v1-0'
API_HOST='https://api.stability.ai'


def chatgpt(user_input, system_settings,chunk):
    if chunk:
        content=split_string_into_chunks(user_input,3000)
    else:
        content=[user_input]
    for x in content:
        response = openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'system', 'content': system_settings},
                    {'role': 'user', 'content': user_input}],
            stream=True   #جعل الرد يصل اول باول
        )
        for x in response:
            if x.choices[0].finish_reason!='stop':
                yield x.choices[0].delta.content # type: ignore
    


def split_string_into_chunks(user_input, chunk_size):
    chunks=[]
    string_length=len(user_input)
    for i in range(0,string_length,chunk_size):
        if i+chunk_size<=string_length:
            chunks.append(user_input[i:i+chunk_size])
        else:
            chunks.append(user_input[i:string_length])
        
    return chunks



def diffusion(prompt):
    response=requests.post(
        f'{API_HOST}/v1/generation/{ENGINE_ID}/text-to-image',
        headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization':f'Bearer {stablediffusion_api_key}'
        },
        json={
            'text_prompts':[
                {
                    'text':prompt
                }
            ],
            'cfg_scale':7,
            'hight':1024,
            'width':1024,
            'samples':1,
            'steps':30
        },
    )
    data=response.json()
    return data['artifacts'][0]['base64']



def transcribe_func(path):
    with open(path, 'rb') as audio_file:
        transcript = openai.Audio.transcribe('whisper-1', audio_file)
    return transcript['text']
         