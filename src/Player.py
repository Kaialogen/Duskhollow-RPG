from math import floor
from Weeapon import iron_sword
from Health_Bar import HealthBar


class Player:
    def __init__(self, dexterity: int, name: str = "Kael", health: int = 50) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.default_weapon = iron_sword
        self.dexterity = dexterity
        self.weapon = self.default_weapon
        self.health_bar = HealthBar(self, colour="green")

        self.dexterity_modifier = floor((self.dexterity - 10) / 2)

    def melee_attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(
            f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}"
        )

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a {self.weapon.name}")

    def drop(self) -> None:
        print(f"{self.name} dropped {self.weapon.name}")
        self.weapon = self.default_weapon
