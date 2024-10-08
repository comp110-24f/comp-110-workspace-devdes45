"""Challenge question 4: defines concat"""

__author__ = "730755654"


def concat(word_1: str, word_2: str) -> str:
    # returns 2 words together
    return word_1 + word_2


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
