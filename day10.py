#!/bin/python3

# this is a great interview question!
# https://www.hackerrank.com/challenges/30-binary-numbers

import sys


n = int(input().strip())

bin_n = bin(n)[2:]

num_1s = 0
run_of_1s = 0
max_1s = 0
prev_1 = False

# consecutive ones!!!!!
# if bin_n[0] == '1':
#    run_of_1s = 1
# else:
#    run_of_1s = 0

#print(bin(n))

for c in str(bin_n):
    if c == '1':
        num_1s = num_1s+1
        if prev_1 == True: # add a one
            run_of_1s = run_of_1s+1
        else: # set the run to 1 consecutive.
            run_of_1s = 1
        prev_1 = True
    else:
        prev_1 = False
        if run_of_1s > max_1s:
            max_1s = run_of_1s
        run_of_1s = 0
    #print(c + ': ' + str(num_1s) + ' : ' + str(run_of_1s) + ': ' + str(max_1s))

# check for final trailing 1 case where last set of consecutive ones is the longest.
if run_of_1s > max_1s:
    max_1s = run_of_1s

#print(num_1s)
print(max_1s)
