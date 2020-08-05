# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:29:19 2020

@author: guanhua
"""


'''
Given an array of integers arr and an integer thres, find a positive integer divisor that ceiling divides all the array by it and sum the result
of the ceiling division. Find the smallest divisor such that the result is less than or equal to the threshold.

https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
'''

import re

n = '[2,3,5,7,11], 11'
n = n.split(', ')
integers = re.findall('\d+', n[0])
integers = [int(x) for x in integers]
thres = int(n[1])
# print(integers, thres)

res = []
div = 1
if thres > 0:
    while div <= thres:
        ce = [-(-x//div) for x in integers]
        sum_int = sum(ce)
        # print(f'if divisor is {div}, arr is {ce} and sum of arr is {sum_int}')
        if sum_int <= thres:
            res.append(div)
        div+=1
    print(res[0])
else:
    print(-1)