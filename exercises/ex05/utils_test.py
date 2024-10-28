import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

"""Defining unit tests"""

__author__ = "730656009"


def test_only_evens_empty_lists():
    """Checks if only_evens returns an empty list for an empty input"""
    assert only_evens([]) == []


def test_only_evens_returns_even_numbers():
    """Checks if only_evens returns only even numbers from input list"""
    assert only_evens([1, 2, 4, 6, 7, 9]) == [2, 4, 6]


def test_only_evens_no_mutations():
    """Checks if only_evens mutates the input list."""
    input = [2, 4, 5]
    answer = only_evens(input)
    assert answer == [2, 4]
    assert input == [2, 4, 5]


def test_sub_negative_index():
    """Checks if sub returns the full list for negative start index"""
    input = [5, 10, 15, 20]
    assert sub(input, -1, 2) == [5, 10]


def test_sub_returns_subset():
    """Checks if sub correctly returns a subset of the input list"""
    input = [1, 5, 7, 12, 16]
    assert sub(input, 1, 4) == [5, 7, 12]


def test_sub_no_mutations():
    """Checks if sub mutates the input list"""
    input = [5, 6, 10, 12]
    answer = sub(input, 0, 2)
    assert answer == [5, 6]
    assert input == [5, 6, 10, 12]


def test_add_at_index_invalid_indices():
    """Checks if add_at_index raises IndexError for an invalid index"""
    # no assert in this test
    with pytest.raises(IndexError):
        add_at_index([0, 1, 2], 2, -2)


def test_add_at_index_adding_values_correctly():
    """Checks if add_at_index correctly inserts an element in the middle"""
    input = [0, 2, 3]
    add_at_index(input, 1, 1)
    assert input == [0, 1, 2, 3]


def test_add_at_index_mutations():
    """Checks if add_at_index mutates the input list correctly"""
    input = [1, 2, 3]
    add_at_index(input, 0, 0)
    assert input == [0, 1, 2, 3]
