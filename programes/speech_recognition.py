# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 13:18:19 2020

@author: Admin

import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    text = r.listen(source)
    try:
        recognised_text = r.recognize_google(text)
        print(recognised_text)
    except sr.UnknownValueError:
        print(" ")
    except sr.REquestError as e:
        print(" ")
""" 
import speech_recognition as  sr

r=sr.Recognizer()
with sr.Microphone() as source:
    text = r.listen(source)
    print('start')
    
try:
    recognised_text = r.recognize_google(text)
    print(recognised_text)
    print ("audio file contant: "+r.recognize_google(text))
except sr.UnknownValueError:
    print ("audio file contant with Unknown exception")
except sr.RequestError:
    print ("audio file contantfr gksdrl;ktgeros ldsfk gsd ")