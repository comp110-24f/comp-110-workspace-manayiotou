"""Creating a game of Wordle"""

__author__ = "730656009"


def input_guess(secret_word_length: int) -> str:
    guess: str = input(f"Enter a {secret_word_length} character word: ")

    while len(guess) != secret_word_length:
        guess = input(
            f"That wasn't {secret_word_length} chars! Try again: "
        )  # changes guess to whatever is inputted after prompted to try again
    else:
        print(guess)
        return guess


def contains_char(secret_word: str, char: str) -> bool:
    """Checking each indices of secret_word to see if it matches with char"""

    assert len(char) == 1

    index: int = 0
    while index < len(secret_word):
        if char == secret_word[index]:
            return True
        index += 1
    return False


def emojified(word_guess: str, word_secret: str) -> str:
    """Compare guess and secret word seeing which chars in the right place or exist"""
    assert len(word_guess) == len(word_secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
