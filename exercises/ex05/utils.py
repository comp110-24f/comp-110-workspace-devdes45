"""EX04 - Utils - Creating function lists."""

__author__ = "730755654"


def only_evens(get_list: list[int]) -> list:
    even_list: list[int] = []
    # loops over every element and checks if they are even to add to new list
    for i in get_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


def sub(get_list: list[int], sindex: int, eindex: int) -> list:
    sub_list: list[int] = []
    # checks if list is empty, indexes are not in range
    if len(get_list) == 0 or sindex >= len(get_list) or eindex <= 0:
        return sub_list
    # checks if start index is below 0 and end index is above length of list
    if sindex < 0:
        sindex = 0
    elif eindex > len(get_list) - 1:
        eindex = len(get_list)
    # checks for characters in the list for the given range
    for i in range(sindex, eindex):
        sub_list.append(get_list[i])
    return sub_list


def add_at_index(get_list: list[int], element: int, index: int) -> None:
    # checks if index is out of range
    if index < 0 or index > len(get_list):
        raise IndexError("Index is out of bounds for the input list")
    get_list.append(0)
    i = len(get_list) - 1
    # moves all elements after the index to the right and adds element to index
    while index < i:
        get_list[i] = get_list[i - 1]
        i -= 1
    get_list[index] = element
