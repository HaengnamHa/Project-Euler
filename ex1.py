# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 20:35:38 2019

@author: ahnka
"""
sum = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum  += i
print(sum)
    
