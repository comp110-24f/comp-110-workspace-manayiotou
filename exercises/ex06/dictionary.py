"""Practice with dictionary functions"""

__author__ = "730656009"


def insert(input: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values of a list"""
    invert: dict[str, str] = {}
    for key, value in input:
        if value in invert:
            raise KeyError("error message of your choice here!")
        invert[value] = key
    return invert


def favorite_color(input: dict[str, str]) -> str:
    """Identifying the most popular color"""
    count_color = {}
    for value in input:
        count_color[value] = count_color.get(value, 0) + 1
    popular_color = "None"
    max_count = 0

    for value in input:
        if count_color[value] > max_count:
            popular_color = value
            max_count = count_color[value]
    return popular_color


def count(input: list[str]) -> dict[str, int]:
    """Counting frequency of items in dictionary"""
    counting: dict[str, int] = {}

    for item in input:
        if item in counting:
            counting[item] += 1
        else:
            counting[item] = 1

    return counting


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """alphabetizing items in list based on first letter"""
    result: dict[str, list[str]] = {}
    for word in input:
        first_letter = word[0].lower()

    if first_letter not in result:
        result[first_letter] = []

    result[first_letter].append(word)

    return result


def update_attendence(input: dict[str, list[str]], day: str, student: str) -> None:
    """Update the attendance log with the student's attendance for the specified day."""
    if day not in input:
        input[day] = []
    if student not in input[day]:
        input[day].append(student)
