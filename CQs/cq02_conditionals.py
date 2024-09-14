"""Practice with Conditionals, Local Variables, and Inputs"""

__author__ = "730656009"


def guess_a_number() -> None:
    secret: int = 7
    x: int = int(input("Guess a number:"))
    print("Your guess was " + str(x))
    if x == secret
        print("You got it!")
    if x > secret
        print("Your guess was too high! The secret number is " + str(secret))
    else 
        print("Your guess was too low! The secret number is " + str(secret))
guess_a_number()
