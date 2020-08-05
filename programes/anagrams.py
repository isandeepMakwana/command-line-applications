# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:51:05 2020

@author: Admin
"""
import sys
def  main():
    """Help user bulid anagratm phase for their name"""
    name = ''.join(ini_name.lower().split())
    name = name.replace('-','')
    limit= len(name)
    phrase =''
    
    running = True
    
    while running:
        temp_phrase = phrase.replace(' ','')
        if len(temp_phrase)<limit:
            print("length of anagram pharase= {}".format(len(temp_phrase)))
            
            find_anagrams(name, dict_file)
            print("Current anagrame phrase =", end=" ")
            print(phrase, file=sys.stderr)
    
            choice,name = process_choice(name)                
            phrase += choice + ' ' 
            
        elif len(temp_phrase) == limit:
            print("\n*****FINISHED!!!*****\n")                
            print("Anagram of name =", end=" ")                
            print(phrase, file=sys.stderr)                
            print()             
            try_again = input('\n\nTry again? (Press Enter else "n" to quit)\n ')                
            if try_again.lower() == "n":
                    running = False
                    sys.exit()  
                    else:                 
                        main()
                        
main()