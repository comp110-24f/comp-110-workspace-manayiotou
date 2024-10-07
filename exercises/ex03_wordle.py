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

    index: int = 0
    accuracy: str = ""

    while index < len(word_guess):
        if (
            word_guess[index] == word_secret[index]
        ):  # when the letter is in secret word and right spot
            accuracy += GREEN_BOX
        elif contains_char(
            word_secret, word_guess[index]
        ):  # when letter is in secret word but different spot
            accuracy += YELLOW_BOX
        else:
            accuracy += WHITE_BOX  # when letter is not in secret word
        index += 1
    return accuracy


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    max_turns: int = 6  # needed max to compare to turn you are on
    win: bool = False

    while turn <= max_turns:
        print(f"=== Turn {turn}/{max_turns} ===")

        guess: str = input_guess(
            len(secret)
        )  # calls input_guess to aquire the word being guessed
        result: str = emojified(
            guess, secret
        )  # calls emojified to compare guess word to secret word

        print(result)  # print emojis to see what letters are in the right place

        if guess == secret:
            win = True
            break
        else:
            turn += 1
    if win:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
