#!/usr/bin/env python

import sys

def staircase(n):
    for i in range(1, n+1):
         print(("#" * i).rjust(n))

def validate_input(n):
    if (n <= 0):
    	raise ValueError('n must be > 0.')

    if (n > 100):
        raise ValueError('n must be <= 100.')

if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError('Please provide n.')

    n = int(sys.argv[1])
    validate_input(n)
    staircase(n)