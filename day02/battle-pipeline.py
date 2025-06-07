def battle(hero, monster):
    if len(hero) > len(monster):
        return hero
    elif len(monster) > len(hero):
        return monster
    elif len(monster) == len(hero):
        return "Draw"


heroes = ["Knight", "Archer", "Mage", "Cleric"]
monsters = ["Slime", "Orc", "Chocobo", "Dragon"]
pacifist = ["Cleric", "Chocobo"]

pairings = [(hero, monster) for hero in heroes for monster in monsters]
print(pairings)
winners = [battle(hero, monster) for (hero, monster) in pairings if hero not in pacifist and monster not in pacifist]
print(winners)