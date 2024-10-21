"""Examples of dictionary syntax with Ice Cream shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluates to number to the number of entries
# print(len(ice_cream))

# add key value
# ice_cream["mint"] = 3

# print(ice_cream["chocolate"])  # prints 12

# test if "pbj" is a key in ice_cream
# has_pbj: bool = "pbj" in ice_cream

# to remove, we use the pop method and give a key
# ice_cream.pop("strawberry")

# to iterate over every key in a loop, use for in
# for flavor in ice_cream:
# tally: int = ice_cream[flavor]
# print(f"{flavor} has {tally} orders")
