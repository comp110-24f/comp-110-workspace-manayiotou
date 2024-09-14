"""Practice with Conditionals, Local Variables, and Inputs"""

__author__ = "730656009"


def guess_a_number() -> None:
    secret: int = 7
    x: int = int(input("Guess a number:"))
    print("Your guess was " + str(x))
    if x == int(secret):
        print("You got it!")
    else:
        if x > int(secret):
            print("Your guess was too high! The secret number is " + str(secret))
        else:
            print("Your guess was too low! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
