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
    character: str = input("Enter a single character: ")

    if len(character) != 1:
        print("Error: Character must be a single character.")
    print(character)
    return character  # function needs a return statement


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    index = 0
    count = 0
    while index < len(word):
        if word[index] == letter:  # checking letter in word to see if it matches
            print(letter + " found at index " + str(index))
            count += 1  # counting how many times the letter appears in the word
        index += 1
        print(str(count) + "instances of " + letter + " found in " + word)
    index += 1
    # if no matches are found in the word
    if count == 0:
        print("No instances of " + letter + " found in " + word)


guess = input_word()
character = input_letter()
contains_char(word=guess, letter=character)
