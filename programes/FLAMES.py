# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 06:40:26 2020

-@author: sandeep Makwana
"""

import string
def remove_matching_letter(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            '''print("inside the loops ")
            print(l1[i],end=" ")
            print(l2[j],end=" ")'''
            if l1[i]==l2[j]:
                #print("under the if condtion")
                c=l1[i]
                l1.remove(c)
                #print(l1)
                l2.remove(c)
                #print(l2)
                l=l1+['*']+l2
                #print(l)
                #print("under the functin --")
            
                return[l,True]
    l=l1+["*"]+l2
    
    #print(l)
    return[l,False]
p1=input("Enter First Person Name :")
p1=p1.lower()
p1=p1.replace(" ","")

p2=input("Enter Second Person Name :")
p2=p2.lower()
p2=p2.replace(" ","")

l1=list(p1)
#print(l1)
l2=list(p2)
#youvrajprint(l2)

account =len(l1)*len(l2)
proceed =True
a=0
while a<account:
    ret_list = remove_matching_letter(l1,l2)
    con_list=ret_list[0]
    #print(con_list)
    proceed=con_list[1]
    star_index=con_list.index('*')
    l1=con_list[:star_index]
    l2=con_list[star_index+1:]
    #print("under the proceed ----------")
    a=a+1;

count =len(l1)+len(l2)
result=['Friends','Love','Affection','Marriage','Enemy','Sibling']

while len(result)>1:
    split_index=(count%len(result))-1
    if split_index>=0:
        R=result[split_index+1:]
        L=result[:split_index]
        result=R+L
    else:
        result=result[:len(result)-1]
    #print(result)

print(result[0])