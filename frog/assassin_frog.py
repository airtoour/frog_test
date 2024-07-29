import random
from frog.frog import Frog


class AssassinFrog(Frog):
    def __init__(self):
        super().__init__()
        self.base_health = int(self.base_health * 1.25)
        self.current_health = self.base_health

    def attack_value(self) -> int:
        return random.randint(self.base_attack // 2, self.base_attack)

    def defense_value(self) -> int:
        return random.randint(0, self.base_armor)