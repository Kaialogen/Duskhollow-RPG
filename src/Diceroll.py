import random

class DiceRoll:
    def __init__(self) -> None:
        pass
        
    def rollD20(self) -> int:
        return random.randint(1, 20)