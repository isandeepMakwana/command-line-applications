# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:03:27 2020

@author: Admin
"""
import string
a=input()
d=int(a)
m=input()
c=[]
B=[]
nolist=list(string.ascii_letters)
c.append(m)
letter=list(c[0])
t=0
s=0
while(t<d):
    for k in range(len(nolist)):
        if(letter[t]==nolist[k]):
            s+=1
    t+=1
if(s==d):
    
    for i in range(0,d):
        q=ord(letter[i])
        if (q<97):
            B.append(chr(155-q))
            m=1
        else:
            B.append(chr(219-q))
            m=1
else:
    print("Invalid")
    
if (m==1):
    print("".join(B),end="")
    




