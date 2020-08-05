# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 21:53:36 2020

@author: Admin
"""

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import pyttsx3 as p

def wiki(query):
    driver=webdriver.Chrome('D:\Python\chromedriver.exe')
        
    driver.get(url="https://www.wikipdia.org/")
    search = driver.find_element_by_xpath('//*[@id="searchInput"]')
    search.click()
    search.send_keys(query+Keys.ENTER)
    # the definition the bot cat be read.
    info = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[3]/ul/li[1]/div[2]')
    readable_text = info.text
    engine= p.init()
    engine.say(readable_text)
    engine.runAndWait()
    
    
    
    

bot=wiki('liberty ball')
