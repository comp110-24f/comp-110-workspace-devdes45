"""Challenge question 4: defines get_coords"""

__author__ = "730755654"


def get_coords(xs: str, ys: str) -> None:
    # 2 while loops to loop through 2 variables
    i: int = 0
    while i < len(xs):
        j: int = 0
        while j < len(ys):
            print(f"({xs[i]},{ys[j]})")
            j += 1
        i += 1


if __name__ == "__main__":
    get_coords("12", "34")
