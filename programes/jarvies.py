# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:40:22 2020

@author: Admin
"""

import speech_recognition as  sr
import pyttsx3 as p
from web_automation import *;
r=sr.Recognizer()
engine = p.init()
engine.say("Hello , how can help you?")
engine.runAndWait()
with sr.Microphone() as source:
    text = r.listen(source) 
    try:
        recognised_text = r.recognize_google(text)
        print(recognised_text)
        
        if recognised_text == "Play music" or recognised_text == "play music":
            music()
    except sr.UnknownValueError:
        print ("audio file contant with Unknown exception")
    except sr.RequestError:
        print ("audio file contanter file is no find ")
        
    engine.say("would you like to music say play music.")
    engine.runAndWait()
    text1 = r.listen(source) 
    try:
        recognised_text1 = r.recognize_google(text1)
        print(recognised_text1)
        
        if recognised_text1 == "Play music" or recognised_text1 == "play music":
            music()
    except sr.UnknownValueError:
        print ("audio file contant with Unknown exception")
    except sr.RequestError:
        print ("audio file contan is not find")