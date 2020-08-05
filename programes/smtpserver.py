# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:03:31 2020

@author: Admin
"""


msg = 'hello this msg was sended by python'
server = smtplib.SMTP('smtp.gmail.com', 587)  
server.ehlo()
server.starttls()
server.login('isandeepmakwana1@gmail.com', 'Vandnasharma94') 
for i in range(50):
    
    server.sendmail('isandeepmakwana1@gmail.com', 'ibosamworldit1@gmail.com', 'Subject: So long capitalsquiz%s process.\nDear she , so long and thanks for all the fish. Sincerely, Bob' % (i+1) ) 
    print("send success mail no. ->", i+1)
server.quit()
print('check  your mail ')