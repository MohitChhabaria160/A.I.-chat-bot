import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def openexe(query):
    query=str(query).lower()

    if "visit" in query:
        nameofweb=query.replace("visit ", "")
        link=f"https://www.{nameofweb}.com"
        webbrowser.open(link)
        return True
    elif "launch" in query:
        nameofweb=query.replace("launch ", "")
        link=f"https://www.{nameofweb}.com"
        webbrowser.open(link)
        return True
    elif "open" in query:
        nameoftheapp=query.replace("open ", "")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    elif "start" in query:
        nameoftheapp=query.replace("start ", "")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    

