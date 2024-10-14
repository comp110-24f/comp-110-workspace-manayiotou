"""Writing List Functions"""

__author__ = "730656009"


def get_first(list_1: list[str]) -> str:
    """Return first element"""
    return list_1[0]


def remove_first(list_2: list[str]) -> None:
    "Remove first element from list_2"
    list_2.pop(0)


def get_and_remove_first(list_3: list[str]) -> str:
    "Return and Remove first element"
    first_element: str = list_3[0]
    list_3.pop(0)
    return first_element
