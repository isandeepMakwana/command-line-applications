# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:17:26 2020

@author: Admin
"""
nolist={`,~,!,@,#,$,}
letter=["6","s","w","m","5","f"]
j=0;
while(j<5):
    for i in range(9):
        if(letter[j]==nolist[i]):
            break
    j+=1