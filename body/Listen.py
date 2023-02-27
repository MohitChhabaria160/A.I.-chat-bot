# Hindi or English - Command
# English

# Step - 1
# pip install googletrans==3.1.0a0

# Step - 2
# Three Functions
# 1 - Listen Function 
# 2 - English Translation
# 3 - Connect

import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans==3.1.0a0

# 1 - Listen : Hindi or English

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")

    except:
        return ""
    
    query = str(query).lower()
    return query

# 2 - Translation

from googletrans import Translator
from googletrans import LANGUAGES

def TranslationHinToEng(Text):
    line = str(Text)
    try:
        translate = Translator()
        result = translate.translate(line, dest='en')
        data = result.text
        print(f"You : {data}.")
        return data
    except Exception as e:
        print(f"Error occurred while translating: {e}")
        return ""


# 3 - Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data
