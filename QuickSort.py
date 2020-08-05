# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:36:22 2020

@author: guanhua
"""

'''
Quick-Sort is a divide-and-conquer sorting algorithm. 
The algorithm selects the last element of the array S as the pivot and builds
3 sub-arrays L (Lesser), E (Equal), G (Greater) which elements of the S are segregated
into. This is done recursively until there remains less than 2 elements in the sub-arrays.

The next step is to merge the sub-arrays from the bottom up. Elements of S are replaced in-place
recursively. The mechanics of the replacement is to keep track of the replacement length by incrementing
a counter. And to use the queue data structure to pop (from the start of the sub-arrays) as the value
to replace the original element of array S.
'''

import random

def getSArray(s,t,sm,bg):
    '''
    Parameters
    ----------
    s : int
        smallest number of elements.
    t : int
        largest number of elements.
    sm : int
        smallest value of elements.
    bg : int
        largest value of elements.

    Returns
    -------
    S : list
        sequence array.

    '''
    S = []
    num_elements = random.randint(s,t)
    for j in range(num_elements):
        rand_int = random.randint(sm,bg)
        S.append(rand_int)
    return S

def merge(S, L, E, G):
    i = 0 # index of S
    while len(L) > 0:
        S[i] = L.pop(0)
        i+=1 # increment
    while len(E) > 0:
        S[i] = E.pop(0)
        i+=1
    while len(G) > 0:
        S[i] = G.pop(0)
        i+=1


def quickSort(S):
    if len(S) < 2: # tells the recursion to stop when len(S) < 2 ie. len(S) = 1
        return
    pivot = S[-1]
    L = [x for x in S if x < pivot]
    E = [x for x in S if x == pivot]
    G = [x for x in S if x > pivot]
    
    quickSort(L)
    quickSort(G)

    merge(S, L, E, G)
    

def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i], end =" ") 
    print()

if __name__=='__main__':
    
    # S = [85, 24, 63, 45, 17, 31, 96, 50] # Python data structures' textbook example
    # S = [18, 90, 24, 56, 78, 33, 26, 86, 1, 34, 72]
    S = getSArray(5,20,1,100)
    print ("Given array is:", end ="\n")
    printList(S)
    quickSort(S)
    print("Sorted array is: ", end ="\n")
    printList(S)