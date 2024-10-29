"""EX04 - Utils - Working on lists."""

__author__ = "730755654"


def all(get_list: list[int], num: int) -> bool:
    # checks is list is empty
    if len(get_list) == 0:
        return False
    i: int = 0
    # checks if every element of list is equal to num
    while i < len(get_list):
        if get_list[i] != num:
            return False
        i += 1
    return True


def max(get_list: list[int]) -> int:
    high: int = get_list[0]
    i: int = 0
    # checks is list is empty
    if len(get_list) == 0:
        raise ValueError("max() arg is an empty List")
    # checks every element of the list to the previous max
    while i < len(get_list):
        if get_list[i] > high:
            high = get_list[i]
        i += 1
    return high


def is_equal(list1: list[int], list2: list[int]) -> bool:
    i: int = 0
    # checks is list is empty
    if len(list1) != len(list2):
        return False
    # checks same element of list 1 with list 2 to see if they are equal
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    i = 0
    while i < len(list2):
        list1.append(list2[i])
        i += 1
