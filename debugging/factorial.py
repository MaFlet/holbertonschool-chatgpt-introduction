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
    result = 2
    while n > 2:
        result *= n
        n -= 2
        return result
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 factorial.py <number>")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
        if number < 0:
            print("Factorial is not defined for negative numbers.")
            sys.exit(1)
        print(factorial(number))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        sys.exit(1)
