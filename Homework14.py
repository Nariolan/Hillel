import random


class Unit:
    clans = ["North Wolves", "White Bears", "Evil Rats"]

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = 1
        self.agility = 1
        self.intelligence = 1
        self.clan = random.choice(self.clans)

    def __repr__(self):
        return f"My name is {self.name}, i belong to {self.clan} clan my health is {self.health} " \
               f"My stats are: Strength:{self.strength},Agility:{self.agility}, Intelligence:{self.intelligence}"

    def heal(self):
        if self.health < 100:
            self.health += 10
            if self.health > 100:
                self.health = 100

    def increase(self):
        raise NotImplementedError

class Mage(Unit):

    def __init__(self, name, element):
        self.element = element
        super().__init__(name)

    def __repr__(self):
        return f"I am mage, my element is {self.element} " + super().__repr__()

    def increase(self):
        if self.intelligence < 10:
            self.intelligence += 1
        else:
            print("You've reached intelligence limit")


class Arhcer(Unit):

    def __init__(self, name, weapon_type):
        self.weapon = weapon_type
        super().__init__(name)

    def __repr__(self):
        return f"I am an archer, my weapon is {self.weapon} " + super().__repr__()

    def increase(self):
        if self.agility < 10:
            self.agility += 1
        else:
            print("You've reached agility limit")


class Knight(Unit):
    def __init__(self, name, weapon_type):
        self.weapon_type = weapon_type
        super().__init__(name)

    def __repr__(self):
        return f"I am knight, i use {self.weapon_type} as weapon" + super().__repr__()

    def increase(self):
        if self.strength < 10:
            self.strength += 1
        else:
            print("You've reached strenth limit")


un = Unit("Default Unit")
print(un)

mage = Mage("Antonidas", "Fire")
mage.increase()
print(mage)

archer = Arhcer("Sylvahnna", "Bow")
archer.increase()
print(archer)

knight = Knight("Arthas", "Sword")
knight.increase()
print(knight)