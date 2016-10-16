#!/bin/python3

import sys

n = int(input().strip())

# check constaints

for number in range(10):
#    print(n + ' x ' + i + ' = ' + n*i)
    i = number+1
    print('{} x {} = {}'.format(n, i, n*i))