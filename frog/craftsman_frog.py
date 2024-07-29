import random

from frog.frog import Frog


class CraftsmanFrog(Frog):
    def __init__(self):
        super().__init__()
        self.base_armor = self.base_armor * 2

    def attack_value(self) -> int:
        return random.randint(self.base_attack // 2, self.base_attack)

    def defense_value(self) -> int:
        return random.randint(0, self.base_armor)
