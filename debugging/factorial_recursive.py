#!/usr/bin/python3
"""
This script calculates factorial using recursion
"""
import sys


def factorial(n):
    """
    Caculates the factorial number using recursion and
    accepts input from the command line arguments
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: ./factorial.py <number>")
            sys.exit(1)

        number = int(sys.argv[1])

        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            f = factorial(number)
            print(f)
    except ValueError:
        print("Please enter a valid integer.")