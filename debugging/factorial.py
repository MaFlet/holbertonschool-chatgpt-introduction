#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        return result
    n = factorial(int(sys.argv[1]))
    print('Factorial \n Number')