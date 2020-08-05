# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:43:02 2020

@author: guanhua
"""

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

def merge(arr,L,R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i+= 1
            k+= 1
        else:
            arr[k] = R[j]
            j+= 1
            k+= 1
            
    while i < len(L):
        arr[k] = L[i]
        i+= 1
        k+= 1
    
    while j < len(R):
        arr[k] = R[j]
        j+= 1
        k+= 1


def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 # Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements 
		R = arr[mid:] # into 2 halves 

		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 
	
		merge(arr,L,R)


def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i], end =" ") 
	print() 

if __name__ == '__main__': 
	S = getSArray(5,20,1,100)
	print ("Given array is:", end ="\n") 
	printList(S) 
	mergeSort(S) 
	print("Sorted array is: ", end ="\n") 
	printList(S) 