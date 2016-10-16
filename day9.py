#!/bin/python3

import sys

# recursion

n = int(input().strip())

def factorial(n):
    if n ==1:
        return 1
    return n*factorial(n-1)

print(factorial(n))

