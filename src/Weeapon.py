class weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


iron_sword = weapon(name="Iron Sword", weapon_type="Sword", damage=10, value=10)

Shortsword = weapon(name="Shortsword", weapon_type="piercing", damage=5, value=5)

crossbow = weapon(name="Crossbow", weapon_type="Ranged", damage=20, value=20)

Pseudopod = weapon(name="Pseudopod", weapon_type="Acid", damage=10, value=0)

Bite = weapon(name="Bite", weapon_type="sharp", damage=4, value=0)