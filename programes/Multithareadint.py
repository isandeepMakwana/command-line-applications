# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:33:34 2020

@author:bufferbook
"""
"""
import datetime,time
startTime= datetime.datetime(2029,10,31,0,0,0)
while datetime.datetime.now()<startTime:
    time.sleep(1)
    print ("Time to sleep 1 sec")
print ('program niow startung in Halloweeb 2029')
"""
"""
import threading , time
print('Strat of program.')

def takeAnap():
    time.sleep(5)
    print('Wake up!')
    
threadObj= threading.Thread(target= takeAnap)
threadObj.start()

print('End of program. ')

"""

import threading 
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep':' & '})
threadObj.start()
