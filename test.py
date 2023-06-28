import speech_recognition as sr
from pywhatkit import *
from pyttsx3 import *
from datetime import *
import pyjokes


global abc


engine=init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def bc(a):
    engine.say(a)
    engine.runAndWait()


def abc():
    #b = (input("enter your task:"))
    #print(b)
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("speak now")
            audio = r.listen(source)
            b = r.recognize_google(audio)
            return b
    except:
        print("sorry could'nt recognize")
        return abc()



def time():
    d= datetime.now().strftime("%H:%M:%S")
    print("time is ",d)
    if(d>="00:00:00" and d<"12:00:00"):
        bc("good morning,sir")
    elif(d>="12:00:00" and d<"16:00:00"):
        bc("good afternoon,sir")
    elif(d>="16:00;00" and d<"20:00:00"):
        bc("good evening,sir")
    else:
        bc("good night,sir")
    bc("i'm your personal asssistant, what can i do for you")

time()
while True:

    b = abc().lower()
    if("name" in b):
        bc("my name is thomas,as said before i'm your persoanl assistant.")
        print("you said : {}".format(b))

    elif("hello" in b):
        bc("hello sir,can i know your name.")
        c=input("your name:")
        bc("hello"+c)

    elif("how are you" in b):
        bc("i'm fine, how are you")
        engine.runAndWait()

    elif("i am fine" in b):
        bc("good to hear that")

    elif("i am sorrow" in b):
        bc("i'm feeling bad about that")

    elif ("information" in b):
        bc("just a second sir, i'll search in google")
        print("you said : {}".format(b))
        a = search(b)
        bc("search complete ")

    elif("open youtube" in b):
        bc("yes sir, i'll open youtube.")
        print("you said : {}".format(b))
        a=playonyt(b)

    elif("from wikipedia" in b):
        bc("i'll search about this in wikipedia")
        print("you said : {}".format(b))
        a=info(b,lines=5)

    elif("who made you" in b):
        bc("i was created by Mr.Arshad")
        print("you said : {}".format(b))

    elif("a comedy" in b):
        bc(pyjokes.get_joke())
        print("you said : {}".format(b))

    elif("goodbye" in b):
        e=input("do you want to end if yes type yes else type no:")
        if(e=="yes"):
            bc("bye,sir")
            exit("good bye")
        else:
            abc()
    elif("play" in b):
        playonyt(b)

    elif("comedy clips" in b):
        playonyt("kids comedy clips")

    else:
        print("you said : {}".format(b))
        bc(" i try to find from google with what i heard")
        search(b)

