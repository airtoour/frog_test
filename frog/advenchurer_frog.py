import random

from frog.frog import Frog


class AdventurerFrog(Frog):
    def __init__(self):
        super().__init__()
        self.base_attack = int(self.base_attack * 1.5)

    def attack_value(self) -> int:
        return random.randint(self.base_attack // 2, self.base_attack)

    def defense_value(self) -> int:
        return random.randint(0, self.base_armor)
