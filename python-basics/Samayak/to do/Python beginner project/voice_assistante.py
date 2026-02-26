import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except:
        speak("Sorry, I didn't catch that.")
        return ""
    return query.lower()

speak("Hello, I'm your Python Assistant. How can I help you today?")

while True:
    query = listen()

    if 'time' in query:
        time_str = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time_str}")
    elif 'open youtube' in query:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in query:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
    elif 'play music' in query:
        speak("Playing a random song for you!")
        music_folder = "C:\\Users\\Public\\Music"
        songs = os.listdir(music_folder)
        os.startfile(os.path.join(music_folder, random.choice(songs)))
    elif 'joke' in query:
        jokes = ["Why did the computer show up late? It had a hard drive!", 
                 "I told my computer I needed a break, and it said 'No problem — I’ll go to sleep!'"]
        speak(random.choice(jokes))
    elif 'exit' in query or 'stop' in query:
        speak("Goodbye! Have a great day! 👋")
        break
