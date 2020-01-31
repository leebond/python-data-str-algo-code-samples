# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:28:16 2020

@author: david
"""


def btreeSearch(mylist, target, start, end):
    if start > end:
        print("start cannot be greater than end")
    else:
        mid = (start + end)//2
        if target == mylist[mid]:
            print(mid)
        elif target < mylist[mid]:
            return btreeSearch(mylist, target, start, mid - 1)
        else:
            return btreeSearch(mylist, target, start, mid + 1)
        
if __name__ == '__main__':
    data = [1,2,4,5,6,9,15,16,23,24,34,35,46]
    btreeSearch(data, 4, 0, len(data))