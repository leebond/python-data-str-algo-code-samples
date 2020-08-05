# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:59:02 2020

@author: guanhua
"""
'''
Given a decimal integer, convert to Hexadecimal. Otherwise to return -1.
'''

def decToHex(n, cnt, data):    
    if n < 16:
        return
    dec = n//16
    rem = n%16    
    n = dec
    cnt +=1
    data.append((cnt, dec, rem))   
    decToHex(n, cnt, data)
    
    
if __name__=='__main__':
    try:
        n = 7803 #'1A0' # 7803 # 0
        if n == 0:
            print(-1)
        else:
            dic = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
            n = int(n)
            # arr = [n]
            cnt = 0
            data=[]
            decToHex(n, cnt, data)
            
            res = [(d, r) for (c, d, r) in data]
            out = []
            for d,r in res:
                if r > 9:
                    out.append(dic[r])
                else:
                    out.append(str(r))
            out = out[::-1]
            last = res[-1][0]
            fin = [str(last)] + out
            print(''.join(fin))
    except:
        print(-1)