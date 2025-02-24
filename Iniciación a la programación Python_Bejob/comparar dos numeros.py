# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:52:41 2025

@author: wpomp
"""

def compare(a, b):
        
    if a < b :
        print( f"{a} is less than {b}")
    
    elif a > b :
        print(f"{a} is greater than {b}")
    
    else :
        print(f"{a} is equal to {b}")

compare(2, 3)
compare(3, 2)
compare(3, 3)
