from .conftest import FixedDice


# Test 1: Test ability modifiers
def test_strength_modifier(combatant):
    assert combatant.strength_modifier == 3


def test_dexterity_modifier(combatant):
    assert combatant.dexterity_modifier == 2


# Test 2: Test taking damage
def test_take_damage_updates_health(combatant):
    combatant.take_damage(5)
    assert combatant.health == 15


def test_health_never_below_zero(combatant):
    combatant.take_damage(100)
    assert combatant.health == 0


# Test 3: Test attack roll (non-critical)
def test_attack_roll_hits(combatant):
    dice = FixedDice([15])  # d20 roll

    attack_roll, is_crit = combatant.roll_attack(dice)

    assert attack_roll == 18  # 15 + STR mod (3)
    assert is_crit is False


# Test 4: Test critical hit detection
def test_critical_hit_detection(combatant):
    dice = FixedDice([20])

    _, is_crit = combatant.roll_attack(dice)

    assert is_crit is True


# Test 5: Test damage roll (normal hit)
def test_damage_roll_normal(combatant):
    dice = FixedDice([5])  # weapon damage roll

    damage = combatant.roll_damage(dice, critical=False)

    assert damage == 8  # 5 + STR mod (3)


# Test 6: Test damage roll (critical hit)
def test_damage_roll_critical(combatant):
    dice = FixedDice([5, 6])  # doubled dice

    damage = combatant.roll_damage(dice, critical=True)

    assert damage == 14  # (5 + 6) + STR mod (3)


# Test 7: Test alive status
def test_is_alive(combatant):
    assert combatant.is_alive() is True
    combatant.take_damage(20)
    assert combatant.is_alive() is False
