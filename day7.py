#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

#print(arr)

arr.reverse()
str = ''.join(str(a) + ' ' for a in arr)
print(str.strip())

