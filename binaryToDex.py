#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:23:33 2020

@author: macbook
"""

def binaryToDec(bin_list, cnt, total):
    
    if len(bin_list) == 0:
        print(total)
    else:
        last_elem = bin_list.pop()
        total += int(last_elem)*2**cnt
        cnt+=1
        binaryToDec(bin_list, cnt, total)
    


if __name__=='__main__':
    b = '10101111'
    binary = [x for x in str(b)]
    
    res = [int(x)*2**(len(binary)-i-1) for i, x in enumerate(binary)]
    print(sum(res))
    
    binaryToDec(binary, 0, 0)