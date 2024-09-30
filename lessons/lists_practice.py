"""Basic Syntax of Lists"""

# Create an Empty List
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# Adding an item to a list
my_numbers.append(1.5)  # append function is to add one value at a time to a list

# print(my_numbers)

# Create an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# Modifying by Index
# (becuase lists are mutable)
game_points[1] = 72

# print(game_points)

# Subscription Notation/Indexing
# print(game_points[1])

# Getting Length
# print(len(game_points))
print(game_points)
# Removing an Item From a List
game_points.pop(1)
print(game_points)


# Are duplicates allowed in lists? YES
# grocery_list: list[str] = ["bananas", "eggs", "bananas"]
# grocery_list.append("bananas")
# print(grocery_list)


# Write new function
def display(int_list: list[int]) -> None:
    """Displays all elements of int_list"""

    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)
