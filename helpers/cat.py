import requests
from helpers import genaudio

CAT_FACT_URL = 'https://catfact.ninja/fact'
CAT_GIF_URL = 'https://g.tenor.com/v1/random?q=cat&key=LIVDSRZULELA&limit=1'


def get_cat_fact():
    res = requests.get(CAT_FACT_URL).json()
    output = res['fact']
    print(output)
    return output


def get_cat_gif():
    print('get cat gif')
    res = requests.get(CAT_GIF_URL).json()['results'][0]['media'][0]['gif']
    data = requests.get(res['url']).content
    f = open('temp/img.gif', 'wb')
    f.write(data)
    f.close()
    return 'temp/img.gif'


def get_fact_audio(text):
    path = genaudio.generate_speech(text)
    #path = "audio/factAudio.wav"
    return path
