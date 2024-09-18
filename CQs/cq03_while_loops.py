"""Using while loops to iterate over a string"""

__author__ = "730656009"


def num_instances(phrase: str, search_char: str) -> int:
    count = 0
    index = 0
    while index < len(
        phrase
    ):  # boolean to loop back and keep checking all of phrase for search_char
        if (
            phrase[index] == search_char
        ):  # condition for when a letter in phrase is == to search_char
            count += 1  # when true you add 1 to count variable
        index += 1  # this step goes to the next letter
    return count


num_instances(phrase="Howdy", search_char="H")
