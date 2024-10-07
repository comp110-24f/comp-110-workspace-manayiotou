"""Mutating Functions"""

__author__ = "730656009"


def manual_append(a_list: list[int], value: int) -> None:
    a_list.append(value)


def double(b_list: list[int]) -> None:
    index: int = 0
    while index < len(b_list):
        b_list[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
