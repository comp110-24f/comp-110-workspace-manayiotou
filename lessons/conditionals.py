"""Practice with conditionals"""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10"""
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger."""
    if hungry:  # conditional/boolean expression
        print("go to training table, YAY!")  # "then" block
    else:
        print("Get back to work girl!!")  # "else" block
    print("I'm proud of you<3")  # either way, be kind to yourself


def check_first_letter(word: str, letter: str) -> str:
    """Check if letter is first character of word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="s"))
