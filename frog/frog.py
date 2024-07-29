from abc import ABC, abstractmethod


class Frog(ABC):
    def __init__(self, attack=15, health=150, armor=5):
        self.base_attack = attack
        self.base_health = health
        self.base_armor = armor
        self.current_health = self.base_health

    @abstractmethod
    def attack_value(self) -> int:
        pass

    @abstractmethod
    def defense_value(self) -> int:
        pass

    def take_damage(self, damage: int):
        self.current_health -= max(0, damage)

    def is_alive(self) -> bool:
        return self.current_health > 0

    def __str__(self):
        return self.__class__.__name__