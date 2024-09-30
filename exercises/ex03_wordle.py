"""Creating a game of Wordle"""

__author__ = "730656009"


def input_guess(secret_word_length: int) -> str:
    guess: str = input("Enter a 5 character word: ")

    if len(guess) != 5:
        print("That wasn't 5 chars! Try again: ")
    else:
        print(guess)
