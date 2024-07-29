import random

from frog.frog import Frog
from frog.assassin_frog import AssassinFrog
from frog.advenchurer_frog import AdventurerFrog
from frog.craftsman_frog import CraftsmanFrog


def create_random_frog() -> Frog:
    frog_classes = [AssassinFrog, AdventurerFrog, CraftsmanFrog]
    return random.choice(frog_classes)()


async def battle(frog1: Frog, frog2: Frog) -> int:
    while frog1.is_alive() and frog2.is_alive():
        damage = frog1.attack_value() - frog2.defense_value()
        frog2.take_damage(damage)

        if not frog2.is_alive():
            return 1

        damage = frog2.attack_value() - frog1.defense_value()
        frog1.take_damage(damage)

        if not frog1.is_alive():
            return 2


async def run_battles(num_battles: int, results: list, classes_participated: list):
    for _ in range(num_battles):
        frog1 = create_random_frog()
        frog2 = create_random_frog()

        classes_participated.append((str(frog1), str(frog2)))

        winner = await battle(frog1, frog2)
        results[winner - 1] += 1
