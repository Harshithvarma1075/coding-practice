'''
import pyttsx3
engine = pyttsx3.init( )
def talk(text):
    engine.say(text)
    engine.runAndWait( )
talk("hello boss i am jarvis")

'''
'''
import speech_recognition as sr
def take_command( ):
    r = sr.Recognizer( )

    with sr.Micropone( ) as source:
        print("Listening..............")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing..........")
        command = r.recognize_google(audio)
        print("you said: ",command)
    except Exception:
        return "none"
    return command.lower( )
'''

import pyttsx3

engine = pyttsx3.init()

def talk(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = input("You: ").lower()
    return command

talk("Hello boss, I am Jarvis. How can I help you?")

while True:
    command = take_command()

    if "hello" in command or "hi" in command:
        talk("Hello boss! Nice to hear from you.")

    elif "how are you" in command:
        talk("I am functioning perfectly. What about you?")

    elif "your name" in command:
        talk("I am Jarvis, your personal assistant.")


    elif "exit" in command or "stop" in command:
        talk("Goodbye boss. Have a great day!")
        break

else:
    talk("Sorry boss, I didn't understand that. Can you say it again?")
