import pytest
from game.combatant import Combatant
from game.weapon import Weapon


class FixedDice:
    def __init__(self, rolls):
        self.rolls = rolls
        self.index = 0

    def roll(self, sides: int, times: int = 1) -> int:
        total = 0
        for _ in range(times):
            total += self.rolls[self.index]
            self.index += 1
        return total

    def rollD20(self) -> int:
        return self.roll(20)


@pytest.fixture
def sword():
    return Weapon("Test Sword", "slashing", (1, 8), 0)


@pytest.fixture
def combatant(sword):
    return Combatant(
        name="Test Fighter",
        health=20,
        armour_class=15,
        dexterity=14,
        strength=16,
        weapon=sword,
        health_bar_colour="default",
    )
