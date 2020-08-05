# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:51:15 2020

@author: Sandeep Makwana

"""

def Checkcondition(n):
    if not n%2==0:
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")

def staircase(n):
    for i in range(n,0,-1):
        if i!=1:
            print(' '*(i-1),'#'*(n-i+1))
        else:
             print(' '*(i-3),'#'*(n-i+1))