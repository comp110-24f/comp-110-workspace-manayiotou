"""List Utility Functions"""

__author__ = "730656009"


def all(input: list[int], given: int) -> bool:
    """Checks if all values in list match the given value"""
    if len(input) == 0:  # for empty lists
        return False
    for num in input:
        if num != given:  # for any int in list that doesn't equal the given int
            return False
    return True


def max(input: list[int]) -> int:
    """Returns largest value in list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_num = input[0]
    for num in input:  # looping over every element to find largest value
        if num > max_num:
            max_num = num  # replace first max_num with the new largest value
    return max_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checking if list 1 and 2 are the same"""
    if len(list_1) != len(list_2):  # checks if lists are the same length
        return False

    for index in range(len(list_1)):  # looping over index in the range of list length
        if list_1[index] != list_2[index]:
            return False
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    index = 0
    while index < len(list_2):
        list_1.append(list_2[index])
        index += 1
    print(list_1)
