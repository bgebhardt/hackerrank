#!/bin/python3

import sys

# from __future__ import print_function

n = int(input().strip())

#n1 = int(input().strip())
#n2 = int(input().strip())



list(map(print,range(1,n)))
# print out range of numbers.  Need to learn what the * operator is doing. :)
print(*range(1,n+1), sep='')



#!/bin/python3

import sys

n = int(input().strip())
print(*range(1,n+1), sep='')


# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:   # can be divided by 400
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap = True
#
#     return leap


#arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

#print(arr)

# arr.reverse()
# str = ''.join(str(a) + ' ' for a in arr)
# print(str.strip())

