#!/bin/python3

import sys

# global dictionary
phone_book = {}

def process_entry(e):
    entry = e.split(' ')
    phone_book[entry[0]] = int(entry[1])
    return

def search_number(search):
    if search in phone_book.keys():
        return str(search + '=' + str(phone_book[search]))
    return 'Not found'


num_entries = int(input().strip())

# get entries
for i in range(num_entries):
    process_entry(input().strip())

# get searches
# This is major hacky... would clean this up if I wasn't lazy. :)
searches = []
search = 'EMPTY'
while search != "": # what is the end of searches?
    try:
        search = input().strip()
        if search != "":
            searches.append(search)
    except EOFError:
        break;

#print(phone_book)

# do searches
for search in searches:
    print(search_number(search))
