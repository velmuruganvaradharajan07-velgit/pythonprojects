import pyautogui as pui
import subprocess as sp
import os
import pyttsx3
import time
def speech():
    words=("Hello,Prakash Thanks For Your time. Let me show the quick demo on the MIMS Automation. I have done this automation using python and "
           "used IDE Pycharm")


    engine = pyttsx3.init()

    engine.setProperty('rate', 210)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    engine.say(words)
    engine.runAndWait()


def functionality():
    os.startfile("C:\\Users\\VV1205\\OneDrive - Hitachi Energy\\Desktop\\MIMS 2.4.0.0.lnk")
#sp.Popen("C:\\Users\\VV1205\\OneDrive - Hitachi Energy\\Desktop\\Postman.lnk")
    print(pui.size())
    print(pui.position())
    time.sleep(2)
    print("Maximize the window")
    pui.moveTo(2093,237,duration=1)
    pui.click(button="left")
    print("Clicking the time Duration")
    pui.moveTo(89,259,duration=1)
    pui.click(button="left")
    print("Selecting option")
    pui.moveTo(301,480,duration=1)
    pui.click(button="left")
    print("Chosing on Change")
    pui.moveTo(301, 580,duration=1)  #changes
    pui.click(button="left")
    print("Saving")
    pui.moveTo(297, 569,duration=1)
    pui.click(button="left")
    print("saving")
    pui.moveTo(1219, 849,duration=1)
    pui.click(button="left")
    print("Saving the changes")
    pui.moveTo(2559, 24, duration=1)
    print("closing the program")
    pui.click(button="left")
    # os.close()


speech()
functionality()