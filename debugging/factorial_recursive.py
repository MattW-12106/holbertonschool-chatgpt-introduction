#!/usr/bin/python3
"""
This script calculates and prints the factorial of a number
passed as a command-line argument.

Usage:
    ./factorial.py <number>
    python3 factorial.py <number>
"""

import sys

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of n.

    Example:
        factorial(5) returns 120
    """
    if n == 0:
        # Base case: factorial of 0 is 1
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

# Convert the first command-line argument to an integer
f = factorial(int(sys.argv[1]))

# Print the factorial result
print(f)
