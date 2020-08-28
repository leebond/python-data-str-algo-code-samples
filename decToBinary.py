#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:50:50 2020

@author: guanhua
"""

def decToBinary(n, remainder_list):
    val = n//2
    remainder = n%2
    remainder_list.append(remainder)
    if val == 0:
        binary = [str(x) for x in remainder_list[::-1]]
        print(''.join(binary))
    else:
        decToBinary(val, remainder_list)
    
if __name__ == '__main__':
    myval = 192
    print(f'Given {myval}:', end='\n')
    decToBinary(myval,[])