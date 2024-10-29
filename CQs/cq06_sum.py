"""Summing the elements of a list using different loops"""

__author__ = "730755654"


def w_sum(vals: list[float]) -> float:
    sum = 0.0
    # checks if list is empty
    if len(vals) == 0:
        return sum
    i = 0
    # adds every element using while loop
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum = 0.0
    # checks if list is empty
    if len(vals) == 0:
        return sum
    # adds every element using for loop
    for i in vals:
        sum += i
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum = 0.0
    # checks if list is empty
    if len(vals) == 0:
        return sum
    # adds every element using for loop with range 0 to length of lists
    for i in range(0, len(vals)):
        sum += vals[i]
    return sum


print(w_sum([0.9, 1.0, 1.1]))
print(f_sum([0.9, 1.0, 1.1]))
print(f_range_sum([0.9, 1.0, 1.1]))
