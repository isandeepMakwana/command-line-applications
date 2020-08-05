# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:29:30 2020

@author: Admin
"""

import time, subprocess
timeleft = int(input('Enter Your time in secondes: '))
while timeleft>0:
    print (timeleft, end=" ")
    time.sleep(1)
    timeleft =timeleft -1
    
# at the end of the xountdown , play a sound file.
    
subprocess.Popen(['start', 'aa.mp4'], shell=True)
