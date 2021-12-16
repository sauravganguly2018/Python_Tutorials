import os
from typing import Mapping
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib

import speech_recognition

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # It takes input from the user and returns string as an output
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.energy_threshold=1000
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-US')
        print(f"User Said : {query}")
    except Exception as e:
        # print(e)
        print("Say that again please !")
        return "None"
    return query

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Goog Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am lucy sir . Please tell me How can I help you ?")

# For sending email we have to enable less secure apps for gmail
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("sauravganguly2018@gmail.com","password")
    server.sendmail("sauravganguly2018@gmail.com",to,content)
    server.close()

if __name__=='__main__':
    wishMe()
    while True:
        query=takeCommand().lower()

        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            print("Searching in Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=4)
            print(f"Results from Wikipedia :\n{results}")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'play song' in query:
            music_dir="D:\\Downloads\\Video"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, The time is : {strTime}")
            speak(f"Sir, The time is : {strTime}")
        elif 'open vs code' in query:
            codePath="C:\\Users\\acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to saurav' in query:
            try:
                speak("What should I say ?")
                content=takeCommand()
                to="gangulysaurav2020@gmail.com"
                sendEmail(to,content)
                speak("Email has been been sent")
            except Exception as e:
                speak("Sorry ganguly bhai . Email cannot be sent due to some error !")
        elif 'quit' in query:
            exit()
