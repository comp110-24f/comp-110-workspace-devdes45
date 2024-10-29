"""finds and returns largest value in a list and then removes it from the list"""

__author__ = "730755654"


def find_and_remove_max(get_list: list[int]) -> int:
    if len(get_list) == 0:
        return -1
    max_num = get_list[0]
    for i in get_list:
        if i > max_num:
            max_num = i
    i = 0
    while i < len(get_list):
        if get_list[i] == max_num:
            get_list.pop(i)
        else:
            i += 1
    return max_num
