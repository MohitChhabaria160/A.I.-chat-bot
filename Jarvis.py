from brain.aibrain import replybrain
from brain.qna import qestionsanswer
from body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from body.Speak import Speak
from features.Clap import Tester
print(">> Started The Jarvis : Wait For Few Seconds More")
from Main import MainTaskExecution

def MainExecution():
    Speak("Hello Sir")
    Speak("I'm Jarvis, I'm Ready To Assist You Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        elif "whatsapp message" in Data:
            pass

        elif "turn on the tv" in Data:# Specific COmmand
            Speak("Ok..Turning On The Android TV")

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = qestionsanswer(Data)

        else:
            Reply = replybrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        MainExecution()
    else:
        pass

ClapDetect()

