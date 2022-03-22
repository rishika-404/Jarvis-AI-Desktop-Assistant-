import datetime
import main
def Wishme():
    """ Wishme function wish you acc to the time."""
    hour = int(datetime.datetime.now().hour)  # 0 to 24
    if hour >= 0 and hour < 12:
        main.speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        main.speak("Good Afternoon!")
    else:
        main.speak("Good Evening!")

    # main.speak("Hello miss.Rishika,Im jarvis,how may i help you?")
    name=("Jarvis")
    main.speak("Hello, I am your Assistant")
    main.speak(name)


