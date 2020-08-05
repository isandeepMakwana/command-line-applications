# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 23:04:43 2020

@author: Admin
"""

n=input("")
a=list(map(int,n.split(" ")))
ap1=int(a[0])
bp1=int(a[1])
ap2=int(a[2])
bp2=int(a[3])

kp1=0
kp2=0
for i in range(10001):
    ap1+=bp1
    ap2+=bp2
    kp1+=1
    kp2+=1
    if ((kp1==kp2)and(ap1==ap2)):
        print("YES")
        break
    else:
        if (kp1>10000):
            print("NO")
            break