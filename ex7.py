character1 = {
    "name": "Kronk",
    "health": 100,
    "age": 30,
    "strength": 100,
}

character2 = {
    "name": "Yzma",
    "health": 100,
    "age": 70,
    "strength": 10,
}

def fight(character1, character2):
    while character1["health"] > 0 and character2["health"] > 0:
        character1["health"] -= character2["strength"]
        character2["health"] -= character1["strength"]
    if character1["health"] <= 0:
        print(character2["name"], "won!")
    else:
        print(character1["name"], "won!")

fight(character1, character2)