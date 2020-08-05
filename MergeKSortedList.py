# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:30:14 2020

@author: guanhua
"""

'''
Merge K sorted lists

Having K sorted lists, how can you return a sorted list with all the elements from each k list?

'''

import heapq as heap
import random

def getData():
    outer = []
    k = random.randint(2,5)
    samples = list(range(1,20))
    for j in range(k):
        len_k = random.randint(3,10)
        inner = random.sample(samples, len_k)
        inner.sort()
        outer.append(inner)
    return outer

def getMergedHeap(mydata):
    myheap = []
    for d in range(len(mydata)):
        myheap = heap.merge(myheap, mydata[d])
    
    return myheap

if __name__ == '__main__':
    mydata = getData()
    print("Given array of arrays is:", end ="\n")
    print(mydata)
    
    myheap = getMergedHeap(mydata)
    
    print("Sorted array is: ", end ="\n")
    print(list(myheap)) 