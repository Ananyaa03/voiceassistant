
import pyttsx3 as p
import speech_recognition as sr
from Seleniumweb import *
from News import *
import randfacts
from Jokes import *
from Weather import *
import datetime


#instance of class
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return('morning')
    elif hour>=12 and hour<16:
        return('afternoon')
    else:
        return('evening')

today_date=datetime.datetime.now()
#instance of recognizer class
r = sr.Recognizer()

speak("Hello mam , good " + wishme() + "I am your voice assistant..")
speak("Today is" + today_date.strftime("%d") + "of" + today_date.strftime("%B") + "And its currently"+ (today_date.strftime("%I"))+(today_date.strftime("%M"))+(today_date.strftime("%p")))
speak("Temperature in Angul is"+str(temp()) + "degree celsius" + "and with "+str(des()))
speak("What can I do for you?")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print('listening')
    audio = r.listen(source)
    #we will send audio toh google api engine and it converts it to text
    text=r.recognize_google(audio)
    print(text)

if 'what' and 'about' and 'you' in text:
    speak('I am also having a good day mam')
speak('What can I do for you')


with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print('listening...')
    audio=r.listen(source)
    text2=r.recognize_google(audio)

if 'information' in text2:
    speak('You need information related to which topic?')

    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening...')
        audio=r.listen(source)
        infor=r.recognize_google(audio)
        
    speak('searching {} in wikipedia'.format(infor))
    print('searching {} in wikipedia'.format(infor))     
    assist = infow()
    assist.get_info(infor)

elif 'play' and 'video' in text2:
    speak('you want me to play which video?')

    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening...')
        audio=r.listen(source)
        vid=r.recognize_google(audio)
    speak('Playing {} on youtube'.format(vid)) 
    print('Playing {} on youtube'.format(vid)) 
    assist=music()
    assist.play(vid)

elif 'news' in text2:
    print('Sure Mam,Now I will read news for you.')
    speak('Sure Mam,Now I will read news for you.')
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif 'fact' in text2:
    speak('Sure Mam')
    x=randfacts.getFact()
    print(x)
    speak("Did you know that,"+x)

elif 'joke' in text2:
    speak('sure mam,get ready for some chuckles')
    ar=joke()
    print(ar[0])
    speak(ar[0])
    print(ar[1])
    speak(ar[1])



      



