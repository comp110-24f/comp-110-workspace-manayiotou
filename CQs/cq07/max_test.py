from CQs.cq07.find_max import find_and_remove_max

"""Testing the infd_and_remove_max function"""

__author__ = "730656009"


def test_find_and_remove_max_return_value() -> None:
    input = [1, 13, 4, 7]
    assert find_and_remove_max(input) == 13


def test_find_and_remove_max_mutated_list() -> None:
    input = [4, 83, 22, 12]
    find_and_remove_max(input)
    assert find_and_remove_max(input) == [4, 22, 12]


def test_find_and_remove_max_empty_list() -> None:
    input = []
    assert find_and_remove_max(input) == -1
    assert input == []
