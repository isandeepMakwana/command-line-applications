# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 22:18:56 2020

@author: Admin
"""

def Answer(a):
    helf= len(a)//2
    strfront=sorted(''.join(a[:helf]))
    a=a[::-1]
    strback =sorted(''.join(a[:helf]))
    #print(strfront, strback)
    if strfront==strback:
        print("YES")
    else:
        print("NO")  
    return;
    
    
n= int(input())
for i in range(n):
    string=input()
    Answer(string)
        