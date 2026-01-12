from game.dice_roll import DiceRoll


dice = DiceRoll()


# Test 1: Test 20 sided dice works
def test_20_sided_dice():
    result = dice.rollD20()
    assert result >= 1 and result <= 20


# Test 2: Test rolling 10 sided dice once
def test_10_sided_dice_one_roll():
    result = dice.roll(10, 1)
    assert result >= 1 and result <= 10
