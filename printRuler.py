# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:22:09 2020

@author: david
"""

def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


# for i in range(13):
#     ticks = '-'*4
#     if i % 4 == 0:
#         print(ticks+str(i))
#         continue
#     print(ticks)


def draw_ruler(inches, length):
    
    for i in range(inches+1):
        if i == 0:
            draw_line(length, '0')
        else:
            draw_interval(length - 1)
            draw_line(length, str(i))


if __name__ == '__main__':
    draw_ruler(3,4)