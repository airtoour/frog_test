import asyncio
from battle import run_battles


async def main():
    num_battles = 50
    results = [0, 0]
    classes_participated = []

    task1 = asyncio.create_task(run_battles(num_battles, results, classes_participated))
    task2 = asyncio.create_task(run_battles(num_battles, results, classes_participated))

    await asyncio.gather(task1, task2)

    for frog1_class, frog2_class in classes_participated:
        pass

    print("Результат:")
    print(f"{frog1_class} выйграла {results[0]} раз.")
    print(f"{frog2_class} выйграла {results[1]} раз.")


if __name__ == "__main__":
    asyncio.run(main())
