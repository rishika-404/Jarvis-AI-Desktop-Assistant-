import main as J
def TakeCommand():
    """ IT takes Microsoft input and returns strings o/p"""
    query = ''
    with J.sr.Microphone() as source:
        # r.energy_threshold= 100
        J.r.adjust_for_ambient_noise(source)
        print("Listening....")
        J.r.pause_threshold = 1
        audio = J.r.listen(source)  # let's recognize it
    try:
        print("Recognizing....")
        query = J.r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except J.sr.RequestError:
        J.speak("Sorry, the I can't access the Google API...")
    except J.sr.UnknownValueError:
        J.speak("Sorry, Unable to recognize your speech...")
    except Exception:
        print("Say that again please...")
        return "None"
    return query.lower()

def reply(text_version):
    ## name
    if "name" in text_version or "who are you" in text_version:
        J.speak("My name is JARVIS")

    ## how are you?
    if "how are you" in text_version:
        J.speak("I am fine...")  # date
    if "date" in text_version:
        # get today's date and format it - 9 November 2020
        date= print(J.now.strftime("%Y-%m-%d %H:%M:%S"))
        J.speak(date)  # time
    ##search google
    if "search" in text_version:
        J.speak("What do you want me to search for?")
        keyword = TakeCommand()   # if "keyword" is not empty
        if keyword != '':
            # webbrowser module to work with the webbrowser
            url = "https://google.com/search?q=" + keyword
            J.speak("Here are the search results for " + keyword)
            J.webbrowser.open(url)
            J.sleep(3)

    ## quit/exit
    if "quit" in text_version or "exit" in text_version:
        J.speak("Ok, I am going to take a nap...")
        exit()


#today
def username():
    J.speak("What should i call you sir")
    uname = TakeCommand()
    J.speak("Welcome Mister")
    J.speak(uname)
    columns = J.shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    J.speak("How can i Help you, Sir")

