# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:17:26 2020

@author: Admin
"""
import pyttsx3 as p
engine = p.init()
#voices= engine.getProperty("voices")
#for female 1 and 0 for male
#engine.setProperty("voice",voices[1].id)
#volume=engine.getProperty("volume")
#print(volume)
engine.say("Hello , how can help you?")
engine.say("or kya kaar rhaa haii sandeep ")
engine.runAndWait()
