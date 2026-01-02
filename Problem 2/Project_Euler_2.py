#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 12:36:05 2026

@author: dylanstanden
"""

# here is the function to create and sum the even Fibonacci numbers
def even_fib(N):
    # gives the sum
    total = 0 
    
    # here is the recursive seed
    f_0 = 0
    f_1 = 1
    f_n = 0
    
    # creates the sequence and tests for congruence modulo 2
    while f_n < N:
        f_n = f_1 + f_0
        f_0 = f_1
        f_1 = f_n
        if f_n % 2 == 0:
            total += f_n
        
    # returns the total sum  
    return total

