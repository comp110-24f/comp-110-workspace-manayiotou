"""Calculate the quantity of tea bags, treats, and money needed for a tea party"""

__author__: str = "730656009"


def main_planner(guests: int) -> None:  # always end function def with semicolon
    """Main function putting all the following functions together"""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $" + str(cost(tea_count=int(guests * 2), treat_count=(int(guests * 3))))
    )  # prints this value as string after parameters are made to be integers.


def tea_bags(people: int) -> int:  # function definition with signature
    """Computing number of tea bags based on number of people"""
    return people * 2  # returns total amount of tea bags


def treats(people: int) -> int:
    """Computing # of treats based on # of teas guests are expecting to drink"""
    return int(tea_bags(people=people) * 1.5)  # this line calls tea_bags function


def cost(tea_count: int, treat_count: int) -> float:  # signature
    """Computing cost of tea bags and treats combined"""
    return (
        tea_count * 0.50 + treat_count * 0.75
    )  # returns the cost of tea bags plus cost of treats


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
