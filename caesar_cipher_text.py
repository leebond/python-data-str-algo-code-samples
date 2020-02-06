# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:57:14 2020

@author: david
"""
def encrypt(msg, dictionary):
    '''Returns the cipher text when passed in a message'''
    cipher_text = transform(msg, dictionary)
    return cipher_text

def decrypt(cipher_text, dictionary):
    '''Returns the decrypted message, given the cipher text'''
    msg = transform(cipher_text, dictionary)
    return msg

def transform(msg, dictionary):
    out = [None] * len(msg)
    for i in range(len(msg)):
        if msg[i].isalpha():
            j = ord(msg[i]) - ord('A') ## tells us the shifts
            out[i] = dictionary[j]
        else:
            out[i] = msg[i]
    return ''.join(out)

if __name__ == "__main__":
    shift = 3
    encoder_map = [chr((k+shift)%26+ord('A')) for k in range(26)] ## the modulus provides the wrap-around feature after shifting
    decoder_map = [chr((k-shift)%26+ord('A')) for k in range(26)] ## the modulus provides the wrap-around feature after shifting
    msg = 'WKH HDJOH LV LQ SODB; PHHW DW MRH’V'
    print(decrypt(encrypt(decrypt(msg,decoder_map),encoder_map),decoder_map))