# Akhbaar padhke sunaao
import requests
import json
from win32com.client import Dispatch

def voice(content):
    speaker=Dispatch("SAPI.SpVoice")
    speaker.speak(content)

if __name__=='__main__':
    url="https://newsapi.org/v2/top-headlines?country=nz&apiKey=dff3b182a5664551b4db5d57ce5d426f"
    resp=requests.get(url)
    str1=resp.text
    dict1=json.loads(str1)
    articles_lst=dict1["articles"]

    for item in articles_lst:
        voice(item["content"])
        voice("Moving onto our next news...Please listen carefully !")
    voice("Thanks for using our service for listening recent news !")

    # voice("hello saurav how are you")
