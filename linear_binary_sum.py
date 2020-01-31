# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:17:16 2020

@author: david
"""


def linear_sum(seq, n):
    'Return the sum of the first n numbers of sequence S.'
    if n == 0:
        return 0
    else:
        return linear_sum(seq, n-1) + seq[n-1]

def binary_sum(seq, start, stop):
    '''Return the sum of the numbers in implicit slice S[start:stop].'''
    if stop <= start:
        raise Exception('Start cannot be larger than stop!')
    elif start == stop - 1:
        return seq[start]
    else:
        mid = (start+stop)//2
        # print(mid)
        return binary_sum(seq, start, mid) + binary_sum(seq, mid, stop)

if __name__ == '__main__':
    m = 20000
    s = [x for x in range(m)]
    
    n = 400
    print(linear_sum(s, 200))
    
    print(binary_sum(s, 0, 200))