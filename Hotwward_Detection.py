import os
import speech_recognition as sr

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
    except :
        return "none"    
    return query.lower()

while True:

    wake_up = takeCommand()
    if "wake up" in wake_up:
        os.startfile("C:\\Users\\91969\\Desktop\\jarvis\\jarvis.py")

    