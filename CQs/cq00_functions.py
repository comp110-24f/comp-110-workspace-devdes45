"""Challenge Question 1"""

__author__ = "730755654"


def mimic(message: str) -> str:
    """Repeats the user's message"""
    return message


def main() -> None:
    """Prints the output of the mimic function"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
