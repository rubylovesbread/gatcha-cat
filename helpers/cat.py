import requests
from helpers import genaudio

CAT_FACT_URL = 'https://cat-fact.herokuapp.com/facts'
CAT_GIF_URL = 'https://cataas.com/cat/gif'


def get_cat_fact():
    res = requests.get(CAT_FACT_URL).json()[0]
    output = res['text']
    print(output)
    return output


def get_cat_gif():
    print('get cat gif')
    data = requests.get(CAT_GIF_URL).content
    f = open('temp/img.gif', 'wb')
    f.write(data)
    f.close()
    return 'temp/img.gif'


def get_fact_audio(text):
    #path = genaudio.generate_speech(text)
    path = "audio/factAudio.wav"
    return path
