"""EX04 - Utils - Working on lists."""

__author__ = "730755654"


def all(get_list: list[int], num: int) -> bool:
    for i in get_list:
        if i != num:
            return False
    return True


def max(get_list: list[int]) -> int:
    high: int = 0
    if len(get_list) == 0:
        raise ValueError("max() arg is an empty List")
    for i in get_list:
        if i > high:
            high = i
    return high


def is_equal(list1: list[int], list2: list[int]) -> bool:
    i: int = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True

def extend(list1: list[int], list2: list[int]) _> None:
    for i in list2:
        list1.append(i)


