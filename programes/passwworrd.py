# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:48:46 2020

@author: Admin
"""

passwordFile  = open('SecretPasswordFile.txt')
sp= passwordFile.read()
print("Enter YOur password")

tp= input()

if tp == sp:
    print('Access Granted')
    if tp=='12345':
        print('That password is one that an idiot puts on their luggage.')
else :
    print('Acces Dehied ')