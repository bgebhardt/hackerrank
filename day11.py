#!/bin/python3

import sys

arr = []
for arr_i in range(6):
     arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
     arr.append(arr_t)

# https://www.hackerrank.com/challenges/30-2d-arrays

# prints an array of arrays -
# 1 1 1 0 0 0
# 1 1 1 0 0 0
# 1 1 1 0 0 0
# 1 1 1 0 0 0
# 1 1 1 0 0 0
# 1 1 1 0 0 0
#arr = [[1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0]]

#arr = [[-1, -1, -1, 0, 0, 0], [-1, -1, -1, 0, 0, 0], [-1, -1, -1, 0, 0, 0], [-1, -1, -1, 0, 0, 0], [-1, -1, -1, 0, 0, 0], [-1, -1, -1, 0, 0, 0]]

#print(arr)

# find the max sum of the hourglasses for the array

# go through each element of the array and calculate the hourglass sum for that element
# save and return the max sum

# detect an hourglass
# from the element (i,j) it is the some of:
# i,j
# i, j+1
# i, j+2
# i+1, j+1
# i+2, j
# i+2, j+1
# i+2, j+2
# abort addition if at any point you go beyond the array

def hourglass_sum(i, j, arr):
    s = 0
    try:
        s += arr[i][j]
        s += arr[i][j+1]
        s += arr[i][j+2]
        s += arr[i+1][j+1]
        s += arr[i+2][j]
        s += arr[i+2][j+1]
        s += arr[i+2][j+2]
        return s
    except IndexError: # if out of bounds can't be an hourglass
        return 7*-9 # return smallest sum, so it never updates max

#print(hourglass_sum(0,0,arr))
#print(hourglass_sum(1,1,arr))

max_hourglass_sum = 7*-9 # start with smallest sum
t = 0
for i in range(5):
    for j in range(5):
        t = hourglass_sum(i,j, arr)
        #print(t)
        if t > max_hourglass_sum:
            max_hourglass_sum = t

print(max_hourglass_sum)