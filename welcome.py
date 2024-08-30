"""A welcoming test program to start COMP110"""

from random import random

__author__ = "01234567"

print("Welcome to COMP110!")
print("You are in for a fun adventure into programming!")
print("<3 the COMP110 Team!")
print(type(random()))


def sum(num1: int, num2: int) -> int:
    """Add two numbers together."""
    return num1 + num2


print(sum(1, 2))
