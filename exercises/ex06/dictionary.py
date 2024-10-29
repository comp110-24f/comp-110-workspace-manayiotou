"""Practice with dictionary functions"""

__author__ = "730656009"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values of a list"""
    invert_list: dict[str, str] = {}
    for key, value in input.items():
        if value in invert_list:
            raise KeyError("error message of your choice here!")
        invert_list[value] = key
    return invert_list


def favorite_color(input: dict[str, str]) -> str:
    """Identifying the most popular color"""
    if not input:  # Check if the dictionary is empty
        return ""
    count_color: dict[str, int] = {}
    for color in input.values():
        count_color[color] = count_color.get(color, 0) + 1

    popular_color = "None"
    max_count = 0

    for color, count in count_color.items():
        if count > max_count:
            popular_color = color
            max_count = count
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


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """Update the attendance log with the student's attendance for the specified day."""
    if day not in input:
        input[day] = []
    if student not in input[day]:
        input[day].append(student)
