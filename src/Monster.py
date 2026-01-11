from math import floor
from Health_Bar import HealthBar
from Weeapon import Bite, Shortsword, Pseudopod


class Monster:
    def __init__(self, name: str, health: int, armour: int, dexterity: int, weapon) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.armour = armour
        self.dexterity = dexterity
        self.weapon = weapon
        self.health_bar = HealthBar(self, colour="red")

        self.dexterity_modifier = floor((self.dexterity - 10) / 2)

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(
            f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}"
        )

    def __str__(self) -> str:
        return self.name

rat = Monster(name="Rat", health=7, armour=12, dexterity=15, weapon=Bite)
skeleton = Monster(name="Skeleton", health=13, armour=13, dexterity=14, weapon=Shortsword)
slime = Monster(name="Gelatinous Cube", health=84, armour=6, dexterity=3, weapon=Pseudopod)
wolf = Monster(name="Wolf", health=11, armour=13, dexterity=15, weapon=Bite)