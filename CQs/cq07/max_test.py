from CQs.cq07.find_max import find_and_remove_max

"""Testing the infd_and_remove_max function"""

__author__ = "730656009"


def test_find_and_remove_max() -> None:
    input = [1, 13, 4, 7]
    assert find_and_remove_max(input) == 13
    assert find_and_remove_max(input) == [1, 4, 7]

    input = []
    assert find_and_remove_max(input) == -1
