#!/usr/bin/python3
"""
This script calucates factorial number passed a command-line argument
"""
import sys

def factorial(n):
    """"
    Calculate and print factorial of argument.
    Parameters:
    n (int): The number for which the factorial is to be calculated.
    Returns:
    int: Factorial of the given number.
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1
        return result
    f = factorial(int(sys.argv[1]))
    print(f)
