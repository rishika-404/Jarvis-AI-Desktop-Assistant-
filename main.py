import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from time import sleep
import time
import os
import mails
import wishMe
import Takecommands as TC
import pyjokes
import ctypes

now = datetime.datetime.now()
engine = pyttsx3.init('sapi5')
## we can use inbuild voice which is present in the windows by microsoft

voices = engine.getProperty('voices')
## print(voices) #it shows us how many voices we have
engine.setProperty('voice', voices[0].id)
## [0].id is for boy and [1] is for girl here
r = sr.Recognizer()

# #getting browser
# urL='https://www.google.com'
# browser = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs %s"
# webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(browser))
# webbrowser.get('chrome').open_new_tab(urL)



##declare functions
def speak(audio):
    """ fn to recognize our voice and return the text_version of it"""
    engine.say(audio)
    engine.runAndWait()

## wait a second for adjust_for_ambient_noise() to do its thing
sleep(1)
##open software in desktop
def opensoftware(message):
    if "open Vscode" in message:
        speak("opening vscode")
        codepath="C:\\Users\\pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    elif "open spotify" in query or "play music" in query:
        speak("opening Spotify")
        path="C:\\Users\\pc\\AppData\\Roaming\\Spotify\\Spotify.exe"
        os.startfile(path)
    
    elif "open firefox" in query:
        speak("opening firefox..")
        path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        os.startfile(path)
    #you can open anything you want just replace path from your software path.

        

if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe.Wishme()
    speak("Start speaking...")
    while True:
        # listen for voice and convert it into text format
        query = TC.TakeCommand().lower() # give "text_version" to reply() fn
        TC.reply(query)
        opensoftware(query)
    # login of executing task based upon the queries
        if 'wikipedia' in query:
            speak("Searching Wikipedia ......")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            if "stop" in query or "ok" in query:
                speak("Okay no problem!")
                exit()
        elif 'open youtube' in query:
            speak("Opening youtube.")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow website")
            webbrowser.open("stackoverflow.com")

    # for your downloaded music
        # elif "play music" in query:
        #     music_dir="C:\\Users\\pc\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
        #     songs=os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[0]))

        elif "time" in query:
            strtime=now.strftime("%H:%M:%S")
            speak(f"The time is: {strtime}")
            print(strtime)

        elif "send email to rishika" in query:
            try:
                speak("what should i say?")
                content=TC.TakeCommand()
                To="rishikabajaj53@gmail.com"
                mails.SendEmail(To,content)
                speak("Email has been sent!")
            except Exception:
                print("Sorry miss.Rishika im not able to sent the message!")
                speak("Sorry miss.Rishika im not able to sent the message!")
        
        elif "change name" in query:
            speak("What would you like to call me, Sir ") 
            name = TC.TakeCommand()  #only speak name 
            speak(f"Thanks for naming me ")
            speak(f"Now my name is {name}")
            print(f"Now my name is {name}")

        
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Miss.Rishika Bajaj.")

        elif "hello" in query or "hello im speak your name" in query:
            speak("whats your name!") 
            enter=TC.TakeCommand()
            speak(f"Hello {enter},How may i help you!")


        elif 'joke' in query or "Tell me some jokes" in query:
            speak(pyjokes.get_joke())
        
        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        
        elif "why you came to world" in query:
            speak("Thanks to Miss.Rishika, im here to help you out!")

        
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much secounds you want to stop jarvis from listening commands")
            #only speak integer 
            a =TC.TakeCommand()
            a=int(a)
            print(a)
            time.sleep(a)

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        
        elif 'reason for you' in query or 'why are you created' in query:
            speak("I was created as a Minor project by Rishika Bajaj")
            print("I was created as a Minor project by Rishika Bajaj")
        

        elif "write a note" in query:
            speak("What should i write, sir")
            note = TC.TakeCommand()
            file = open('file.txt', 'w')
            if note!=" ":
                speak("Sir, Should i include date and time")
                snfm = TC.TakeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = now.strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
            else:
                speak("What should i write, sir")
                note = TC.TakeCommand()
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("file.txt", "r")
            print(file.read())
            speak(file.read(6))


