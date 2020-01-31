# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:27:30 2020

@author: david
"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_fast(n): ## to return n-1 and n-2 terms
    if n <= 1:
        return (1, 0)
    else:
        n_1, n_2 = fibonacci_fast(n-1)
        fn = n_1+n_2
        return (fn, n_1)
    
if __name__ == '__main__':
    from datetime import datetime
    n = 35
    
    st1 = datetime.now()
    print(fibonacci(n))
    ep1 = datetime.now() - st1
    print(ep1.microseconds)
    
    st2 = datetime.now()
    print(fibonacci_fast(n))
    ep2 = datetime.now() - st2
    print(ep2.microseconds)