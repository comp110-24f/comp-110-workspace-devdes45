"""Challenge question 3"""

__author__ = "730755654"


def num_instances(phrase: str, search_char: str) -> int:
    i = 0
    count = 0
    while i < len(phrase):
        if phrase[i] == search_char:
            count += 1
            i += 1
    return count
