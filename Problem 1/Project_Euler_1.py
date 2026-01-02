#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 11:38:25 2026

@author: dylanstanden
"""

#Project Euler: Multiples of 3 or 5



def cong_sum(N):
    #this is the total sum
    total = 0
    
    #this checks for congruence modulo 3 or 5
    for i in range(1,N): 
        if i % 5 == 0 or i % 3 == 0:
           total += i
    return total

#this prints the answer required for the question
print(cong_sum(1000))
    

