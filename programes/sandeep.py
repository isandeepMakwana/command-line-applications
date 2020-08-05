# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:03:27 2020

@author: Admin
"""

a=input()
d=int(a)
m=input()
c=[]
B=[]
nolist=[]
c.append(m)
letter=list(c[0])

for i in range(0,d):
    q=ord(letter[i])
    if (q<97):
        B.append(chr(155-q))
        m=1
    else:
        B.append(chr(219-q))
        m=1
t=0
while(t<d):
    for k in range(len(nolist)):
        if(letter[t]==nolist[k]):
            m=0
            break
    t+=1
if(m==0):
    print("Invalid")
    
else:
    print("".join(B),end="")
    




