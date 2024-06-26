
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import openai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
wishMe()
speak("I am Jarvis. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    
    except Exception as e:
        return "Some error has occured. Sorry from jarvis"
 

if __name__ == "__main__":

    while True:
        print("listening....")
        query = takeCommand().lower()
       #if "Jarvis" in query:
            #query = query.replace("Jarvis", "")    
                    
        sites = [[ "youtube","https://www.youtube.com"],[ "google","https://www.google.com"]]
        
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        
        if "open music" in query:
            musicPath = "C:\\Users\\prash\\Downloads\\Unlike Pluto - Hollow [NCS Release].mp3"
            os.startfile(musicPath)

        if "wikipedia" in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
        
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strfTime}")

        if "open vscode" in query:
            os.startfile(f"C:\\Users\\prash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

      
        query = query.replace("open", "")
        os.system('start '+query)