#!/bin/python3

import sys

num_test_cases = int(input().strip())

# get test cases
test_cases = []
for i in range(num_test_cases):
    test_cases.append(input().strip())

def print_chars(s):
    """print even and then odd indexed characters"""
    final_string = []
    for i in range(len(s)):
        if i % 2 ==0:
            final_string.append(s[i])

    final_string.append(' ')

    for i in range(len(s)):
        if i % 2 != 0:
            final_string.append(s[i])

    print(''.join(final_string))

for tc in test_cases:
    print_chars(tc)

