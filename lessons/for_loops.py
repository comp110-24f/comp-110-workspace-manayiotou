"""Practice writing for loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]

for elem in pets:
    print(f"Good boy, {elem}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0, len(names)):
    print(f"{str[idx]}: {names[idx]})