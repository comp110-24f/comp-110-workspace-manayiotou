"""Finding max value and removing it"""

__author__ = "730656009"


def find_and_remove_max(input: list[int]) -> int:
    if input == []:
        return -1

    max: int = input[0]
    for num in input:  # loops over elements
        if num > max:
            max = num

    idx = 0
    while idx < len(input):
        if input[idx] == max:  # checks which value in list is considered the max
            input.pop(idx)
        else:
            idx += 1
    return max
