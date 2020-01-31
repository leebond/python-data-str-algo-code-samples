# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:55:49 2020

@author: david
"""


''' 
Quadratic vs Linear Implementation of Prefix Average

A prrefix average is the computation of the average of all the previous values
inclusive of the current value.

eg. given a list [1,2,3,4,5]
At the first element, the average is 1/1 = 1. At 5th element, the average is (1+2+3+4+5)/5 = 3

The functions accept a list as input and iterates through each element and finds the prefix
average
'''
from datetime import datetime
import numpy as np

def prefixAverageQuadratic(mylist):
    out = []
    for i in range(len(mylist)):
        out.append(sum(mylist[0:i+1])/(i+1))
    return out

def prefixAverageLinear(mylist):
    n = len(mylist)
    out = [0] * n
    total = 0
    for i in range(n):
        total += mylist[i]
        out[i] = total/(i+1)
    return out

def prefixAverageLinearNumpy(mylist):
    n = len(mylist)
    arr = np.array(mylist)
    out = np.zeros(n)
    for i in range(n):
        out[i] = np.sum(arr[0:i+1]/(i+1))
    return out.tolist()
                    
    
def check_runtime_quadratic(mylist):
    st1 = datetime.now()
    prefixAverageQuadratic(mylist)
    elapse = (datetime.now()-st1).microseconds
    print("Time spent for list of size %s: %s microseconds" %(LENGTH, elapse))    

def check_runtime_linear(mylist):
    st1 = datetime.now()
    prefixAverageLinear(mylist)
    elapse = (datetime.now()-st1).microseconds
    print("Time spent for list of size %s: %s microseconds" %(LENGTH, elapse)) 

def check_runtime_numpylinear(mylist):
    st1 = datetime.now()
    prefixAverageLinearNumpy(mylist)
    elapse = (datetime.now()-st1).microseconds
    print("Time spent for list of size %s: %s microseconds" %(LENGTH, elapse))
    
if __name__ == '__main__':
    
    LENGTH = 100
    p = [x for x in range(LENGTH)]
    q = [x for x in range(LENGTH*10)]
    r = [x for x in range(LENGTH*10**2)]
    s = [x for x in range(LENGTH*10**5)]
    
    check_runtime_quadratic(p)
    check_runtime_quadratic(q)
    check_runtime_quadratic(r)
    # check_runtime_quadratic(s) ### takes relatively incredulously long!! Try at your own time.

    check_runtime_linear(p)
    check_runtime_linear(q)
    check_runtime_linear(r)
    check_runtime_linear(s)
    
    check_runtime_numpylinear(p)
    check_runtime_numpylinear(q)
    check_runtime_numpylinear(r)
    check_runtime_numpylinear(s)