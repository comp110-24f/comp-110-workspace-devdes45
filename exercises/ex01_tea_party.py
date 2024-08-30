"""Exercice Question 1"""

__author__ = "730755654"


def main_planner(guests: int) -> None:
    """prints the output of all functions below"""
    print("A cozy tea party for", guests, "people")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """returns number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """returns number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """returns cost of treats and tea bags"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
