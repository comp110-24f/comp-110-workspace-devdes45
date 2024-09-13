"""Challenge question 1"""

__author__ = "730755654"


def guess_a_number() -> None:
    secret: int = 7
    guess = input("Guess a number: ")
    print("Your guess was: " + guess)
    if int(guess) > secret:
        print("your guess was too high! The secret number is", secret)
    elif int(guess) < secret:
        print("your guess was too low! The secret number is", secret)
    else:
        print("You got it!")


if __name__ == "__main__":
    guess_a_number()
