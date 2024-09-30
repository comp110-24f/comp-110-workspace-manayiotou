"""coordinates function"""

__author__ = "730656009"


def get_coords(xs: str, ys: str) -> None:
    # two indexes needed for two parameters
    index = 0
    while index < len(xs):
        # inner loop
        index2 = 0
        while index2 < len(ys):

            print(xs[index], ys[index2])
            index2 += 1
        index += 1
