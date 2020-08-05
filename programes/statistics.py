# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:12:45 2020

@author: nptel python
"""
import random
from statistics import mean
from scipy import stats
import matplotlib.pyplot as plt
Estimates = []
for j in range(75):
    i = random.randint(1,2000)
    Estimates.insert(j,i)
y=[]
Estimates.sort()
tv = int(0.1*len(Estimates))
Estimates1 = Estimates[tv:]
Estimates1 = Estimates1[:len(Estimates1)- tv]
Estimates=[i for i in Estimates1]
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates,y,'r--')
a=mean(Estimates)
plt.plot([a],[5],'g^')
plt.ylabel("some values of YY")
plt.xlabel("some values of XX")
"""

plt.plot([1,2,3,4],[1,4,5,16],'r^')


m=stats.trim_mean(Estimates, 0.1)
print(m)

print(mean(Estimates))

Estimates = Estimates[tv:]

"""