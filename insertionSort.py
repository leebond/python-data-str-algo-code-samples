# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:50:20 2020

@author: david
"""


def insertionSort(seq):
    '''We start with the first element in the array. One element by itself
    is already sorted. Then we consider the next element in the array. If it is smaller
    than the first, we swap them. Next we consider the third element in the array. We
    swap it leftward until it is in its proper order with the first two elements. We then
    consider the fourth element, and swap it leftward until it is in the proper order with
    the first three. We continue in this manner with the fifth element, the sixth, and so
    on, until the whole array is sorted.
    '''
    
    for i in range(1, len(seq)):
        cur = seq[i]
        
        # loop to continue swapping leftward: create a while loop that decrements its value
        j = i
        while cur < seq[j-1] and j > 0:
            prev = seq[j-1]
            seq[j] = prev            
            j -= 1
        seq[j] = cur
    return seq

print(insertionSort([3,1,4,2,5]))