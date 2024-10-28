"""Building list utility functions"""

__author__ = "730656009"


def only_evens(input: list[int]) -> list[int]:
    new: list[int] = []
    for num in input:
        if num % 2 == 0:  # seeing if value is even
            new.append(num)
    return new


def sub(input: list[int], start_i: int, end_i: int) -> list[int]:
    new = []
    # all scenarios that return an empty list
    if len(input) == 0:
        return []
    if start_i >= len(input):
        return []
    if end_i <= 0:
        return []
    # reframing indices to fit the range of the list
    if start_i < 0:
        start_i = 0
    if end_i > len(input):
        end_i = len(input)

    for idx in range(start_i, end_i):
        new.append(input[idx])
    return new


def add_at_index(input: list[int], add_elem: int, given_i: int) -> None:
    # scenarios of invalid indices that return indexerror
    if given_i < 0:
        raise IndexError("Index is out of bounds for the input list")
    if given_i > len(input):
        raise IndexError("Index is out of bounds for the input list")
    # making space for the new value in the list
    input.append(0)

    for i in range(len(input) - 1, given_i, -1):
        input[i] = input[i - 1]

    input[given_i] = add_elem
