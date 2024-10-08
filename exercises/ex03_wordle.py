"""EX02 - Wordle - The actual thing."""

__author__ = "730755654"

# global variable used in both main and emojified
GREEN_BOX: str = "\U0001F7E9"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        # new variable for guess accuracy
        emoji: str = emojified(input_guess(len(secret)), secret)
        print(emoji)
        # exits out if word is correct, goes to 6 turns if it isn't
        if emoji == len(secret) * (GREEN_BOX):
            print(f"You won in {turn}/6 turns!")
            return None
        turn += 1
        emoji = ""
    print("X/6 - Sorry, try again tomorrow!")


def input_guess(length: int) -> str:
    """gets user input for guess of correct length"""
    # while loop to iterate input till word length is correct
    real_word: str = input(f"Enter a {length} character word: ")
    while len(real_word) != length:
        real_word = input(f"That wasn't {length} chars! Try again: ")
    return real_word


def contains_char(word: str, letter: str) -> bool:
    """checks if character is in word"""
    assert len(letter) == 1
    i: int = 0
    # while loop to check every character in word for equivalence
    while i < len(word):
        if word[i] == letter:
            return True
        i += 1
    return False


def emojified(real_word: str, guess: str) -> str:
    """returns the wordle accuracy with colored squares"""
    assert len(guess) == len(real_word)
    wordle: str = ""
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    # while loop to check which character is what color square
    while i < len(real_word):
        if guess[i] == real_word[i]:
            wordle += GREEN_BOX
        elif contains_char(word=guess, letter=real_word[i]):
            wordle += YELLOW_BOX
        else:
            wordle += WHITE_BOX
        i += 1
    return wordle


if __name__ == "__main__":
    main(secret="codes")
