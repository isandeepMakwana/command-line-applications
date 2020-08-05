# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:08:54 2020

@author: Admin
"""
"""

import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
"""

import requests ,sys, webbrowser, bs4
#print('Googling...')    # display text while downloading the Google page 
#res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
#res.raise_for_status()


# Retrieve top search result links
File=open('Ram.html') 
soup= bs4.BeautifulSoup(File.read())
#soup = bs4.BeautifulSoup(res.text)
# Open a browser tab for each result. 
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems)) 
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))