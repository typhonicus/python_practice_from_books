# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:43:37 2018

@author: Typhonicus
"""

compendium = {}

while True:
    name = input("Enter in a name: ")
    response = input("Enter what this person's favorite element is: ").lower().strip()
      
    compendium[name] = response
    
    keep_going = input("Wanna add another pair of dictionary pairs? Enter 'n' to quit or any other value to continue: ").lower().strip()
    if keep_going == 'n':
        break
    
for name, response in compendium.items():
    print("{} likes {}.".format(name, response)) 
    
print(compendium)