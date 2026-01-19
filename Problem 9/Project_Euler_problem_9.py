#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 12:36:18 2026

@author: dylanstanden

"""
def triple(n) -> int, tuple:
    
  
   for c in range(1,n):
     for b in range(1,c):
        for a in range(1,b):
            if a**2 + b**2 == c**2 and a + b + c == n:
                return a*b*c, (a,b,c)
