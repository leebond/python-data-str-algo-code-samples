#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:24:11 2020

@author: guanhua
"""

def isInt(d):
    try:
        int(d)
        return True
    except:
        return False

def hexToDec(hex_list, cnt, total):
    if len(hex_list) == 0:
        print(total)
    else:
        last_elem = hex_list.pop()
        if isInt(last_elem):
            val = int(last_elem)
        else:
            dic = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
            val = dic[last_elem]
        total += val * 16**cnt
        cnt+=1
        hexToDec(hex_list, cnt, total)
    
if __name__ == '__main__':
    hex_str = 'ABC'
    
    hex_str = str(hex_str)
    hex_list = [c for c in hex_str]
    hexToDec(hex_list, 0, 0)