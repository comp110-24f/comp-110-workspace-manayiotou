"""Summing the elements of a list using different loops"""

__author__ = "730656009"


def w_sum(vals: list[float]) -> float:
    total = 0.0
    index = 0

    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    total = 0.0
    for elem in vals:
        total += elem
    return total


def f_range_sum(vals: list[float]) -> float:
    total = 0.0
    for index in range(0, len(vals)):
        total += vals[index]
    return total
