from apple import Apple
from plant import Plant
import random

MAX_NUM_OF_NEW_APPLES = 10


class AppleTree(Plant):
    def __init__(self):
        self.age = 1
        self.apples = []

    def __repr__(self):
        return (
            f'{self.__class__.__name__}:\n'
            f'Возраст дерева: {self.age}\n'
            f'Кол-во яблок: {len(self.apples)}\n'
            f'Яблоки: \n{self.apples!r}\n'
        )

    def grow_new_fruits(self):
        for _ in range(random.randrange(MAX_NUM_OF_NEW_APPLES)):
            self.apples.append(Apple())

    def die_fruits(self):
        self.apples = []

    def get_old_good_apples(self):
        old_apples = []
        good_apples = []
        for apple in self.apples:
            if apple.is_ripen():
                old_apples.append(apple)
            else:
                good_apples.append(apple)
        return old_apples, good_apples

    def grow(self):
        self.age += 1
        _, self.apples = self.get_old_good_apples()
        for apple in self.apples:
            apple.mature()

        if 2 < self.age < 5:
            self.grow_new_fruits()

    def is_ripen(self) -> bool:
        return True if all(apple.is_ripen() for apple in self.apples) else False

    def collect_harvest(self) -> list[Apple]:
        old_apples, self.apples = self.get_old_good_apples()
        return old_apples
