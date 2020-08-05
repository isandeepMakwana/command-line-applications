# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:27:14 2020

@author: Admin
"""

#! python3 # mapIt.py - Launches a map in the browser using an address from the # command line or clipboard.
import webbrowser, sys,pyperclip
if len(sys.argv) > 1:    # Get address from command line.    
    address = ' '.join(sys.argv[1:])
    print(address)
# TODO: Get address from clipboard
else:    # Get address from clipboard.    
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
