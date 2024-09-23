"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730656009"


def input_word() -> str:
    # local variable equal whatever word is typed after the given prompt
    guess: str = input("Enter a 5-character word: ")

    # making sure word is exactly 5 letters long
    if len(guess) != 5:
        print("Error: Word must contain 5 characters.")  # if condition is true
    print(guess)  # ex02 require guess to be printed back in every scenario
    return guess  # function needs a return statement


def input_letter() -> str:
    letter: str = input("Enter a single character: ")

    if len(letter) != 1:
        print("Error: Character must be a single character.")
    print(letter)
    return letter  # function needs a return statement


input_word()
input_letter()
