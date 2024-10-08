"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730755654"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """get input word and check if word is correct length"""
    wordle: str = input("Enter a 5-character word: ")
    # Used if statement to see if word is 5 characters long
    if len(wordle) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return wordle


def input_letter() -> str:
    """get input letter and check if letter is correct length"""
    check_letter: str = input("Enter a single character: ")
    # Used if statement to see if word is only 1 character
    if len(check_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return check_letter


def contains_char(word: str, letter: str) -> None:
    """returns instances of input letter in input word"""
    print("Searching for", letter, "in", word)
    i: int = 0
    count: int = 0
    # used while loop to see if each character equals letter or not
    while i < len(word):
        if word[i] == letter:
            print(letter, "found at index", i)
            count += 1
        i += 1
    # used if statements to see what count equals and corresponding print statement
    if count > 1:
        print(count, "instances of", letter, "found in", word)
    elif count == 1:
        print(count, "instance of", letter, "found in", word)
    else:
        print("No instances of", letter, "found in", word)


if __name__ == "__main__":
    main()
