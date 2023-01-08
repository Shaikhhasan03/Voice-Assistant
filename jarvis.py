#Modules
from re import T
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from sketchpy import library as lib
import random
import pyautogui
import keyboard
from time import sleep
import requests
from  bs4 import BeautifulSoup
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def  speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    
    
    elif hour>=12 and hour<18:     
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir!")

def takeCommand():
    #It takes input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=5)
            
    try: 
        print("Recognizing...")
        query= r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("say that again please")
        return "none"    
    return query

def command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
        print("Recognizing...")
        query= r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")


def ff():
  speak("He is born on 10/03/2003 in India.Her study completed in Latur.Later he move to pune to purue her higher degree")

def temperature():
    api ="https://www.google.com/search?q=temperature+in+latur"
    r = requests.get(api)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div",class_="BNeawe").text
    print(temp)
    speak(temp)
d = ["send message","open telegram"]
def taskex():
    wishMe()  
    speak("How may I Help you")

    while True:    
        query=takeCommand().lower() #Converting user query into lower case
      

# code for searching information

        if 'wikipedia' in query:  

            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'youtube search' in query:
            speak("OK SIR, This is what i found for your search")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            
        elif 'google search' in query:
            speak("OK SIR, This is what i found for your search")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)

        elif 'website' in query:
            speak("OK SIR, Launching....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
                 
#code for general information
        
        elif "shut up" in query:
            speak("sorry Sir")

        elif "who are you" in query:
            speak("I am hazel , your desktop assistnt")
        
        elif "you need a break" in query:
            speak("Ok sir,you can call me anytime !")
            break

        elif 'play music' in query:
            music_dir = 'D:\\music\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif ' time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
         
        elif " your name" in query:
            speak("I am hazel .")

        elif "how are you" in query:
            speak("I am well")
            speak("Whats about you sir .")

        elif "fine" in query:
            speak("Thats well sir")


        elif "sketch" in query:
           
            speak("Drawing sir, wait a minute")
            obj = lib.rdj()
            obj.draw()

        elif " birthday"  in query:
            speak("I was born on 10/03/2022 ")
        
        elif " strong password"  in query:
            speak("suggesting sir")
            upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            lower_case = "abcdefghijklmnopqrstuvwxyz"
            num_case = "0123456789"
            symbol_case = "`!@#$%^&*"
            add_case = lower_case + num_case 
            password_length = 8
            password = "".join(random.sample(add_case , password_length))
            print(password)

        elif " password"  in query:
            speak("showing sir")
            lower_case = "abcdefghijklmnopqrstuvwxyz"
            num_case = "0123456789"
            add_case = lower_case + num_case 
            password_length = 8
            password = "".join(random.sample(add_case , password_length))
            print(password)

        elif "who made you" in query:
            speak("I made by brightest man her name is hasan !")
        
        elif "who is your creator" in query:
            speak("Hasan Shaikh is my creator")
        
        elif "who is hasan shaikh" in query:
            ff()
        elif "tell me about your creator" in query:
            ff()
        
        elif "what can you do" in query:
            speak("I can do a lots of things  ")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold=1
                audio = r.listen(source)
                print("Recognizing...")
                query= r.recognize_google(audio,language='en-in')
                print(f"User said:{query}\n") 
                if "close it" in query:
                    speak("Ok sir")
                    os.system("taskkill /f /im chrome.exe")

        
        elif 'open google' in query:
            webbrowser.open("google.com")
            
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold=1
                audio = r.listen(source)
                print("Recognizing...")
                query= r.recognize_google(audio,language='en-in')
                print(f"User said:{query}\n") 
                if "close it" in query:
                    speak("Ok sir")
                    os.system("TASKKILL /f /im chrome.exe")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open playstore' in query:
            webbrowser.open("playstore.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open microsoft store' in query:
            webbrowser.open("microsoftstore.com")        
        elif 'open code' in query:
            os.mummy
            startfile = "C:\\Users\\shaik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            


# code for temperature :
        elif " temperature" in query:    
            api ="https://www.google.com/search?q=temperature+in+latur"
            temperature()
        elif "what is temperature in latur" in query:
            api ="https://www.google.com/search?q=temperature+in+latur"
            temperature()
        elif "what is temperature in mumbai" in query:
            api ="https://www.google.com/search?q=temperature+in+mumbai"
            temperature()
        elif "what is temperature in pune" in query:
            api ="https://www.google.com/search?q=temperature+in+pune"
            temperature()
        elif "what is temperature in london" in query:
            api ="https://www.google.com/search?q=temperature+in+london"
            temperature() 
        elif "what is temperature in delhi" in query:
            api ="https://www.google.com/search?q=temperature+in+delhi"
            temperature()
        elif "what is temperature in kashmir" in query:
            api ="https://www.google.com/search?q=temperature+in+kashmir"
            temperature()
        elif "what is temperature in kolkata" in query:
            api ="https://www.google.com/search?q=temperature+in+kolkata"
            temperature()   

# code for send messages :                  
        
        elif "open telegram" in query:
            speak("opening sir")
            os.startfile("C:\\Users\\91969\\Desktop\\Telegram.lnk")
            speak("whom do you want to send message")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold=1
                audio = r.listen(source)
                print("Recognizing...")
                query= r.recognize_google(audio,language='en-in')
                print(f"User said:{query}\n")                                   
                if "mummy"  in query:
                    pyautogui.click(x=377, y=110)
                    sleep(1)
                    keyboard.write(query)
                    speak("what message do you want to send")
                    command()                
                    sleep(1)
                    pyautogui.click(x=457, y=218)
                    sleep(1)
                    keyboard.write(query)
                    keyboard.press("enter")
                    speak("send sir")
                elif "sana"  in query:
                    pyautogui.click(x=114, y=64)
                    sleep(1)
                    keyboard.write(query)
                    speak("what message do you want to send")
                    command()
                    sleep(1)
                    pyautogui.click(x=95, y=133)
                    sleep(1)
                    keyboard.write(query)
                    keyboard.press("enter")
                    speak("send sir")
                elif "nothing" in query:
                    speak("i shall show you recent messages")
                elif "close it" in query:
                    speak("Ok Sir")
                    os.system("TASKKILL /f /im telegram.exe")
taskex()  