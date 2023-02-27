#rom selenium import webdriver
#rom selenium.webdriver.chrome.options import Options
#rom selenium.webdriver.common.by import By
#mport os
#rom time import sleep
#mport pandas as pd
#rom body.Speak import Speak
#mport pathlib
#rom body.Listen import MicExecution
#mport pyautogui
#
#criptDirectory = pathlib.Path().absolute()
#
#ptions = Options()
#ptions.add_experimental_option("excludeSwitches", ["enable-logging"])
#ptions.add_argument("--profile-directory=Default")
#ptions.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
#s.system("")
#s.environ["WDM_LOG_LEVEL"] = "0"
#athofDriver = "dataBase\\chromedriver.exe"
#river = webdriver.Chrome(PathofDriver,options=options)
#river.maximize_window()
#peak("Initializing The Whatsapp Software.")
#
#istWeb = {'mummy' : "+919893095464",
#           'papa': "+919893016056",
#           "janu": '+916268568686'}
#
#ef WhatsappSender(Name):
#   Speak(f"Preparing To Send a Message To {Name}")
#   Speak("What's The Message By The Way?")
#   Message = MicExecution()
#   Number = ListWeb[Name]
#   LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
#   driver.get(LinkWeb)
#   sleep(7)
#   a=driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
#   a.click()
#   Speak("Message Sent")
#
#