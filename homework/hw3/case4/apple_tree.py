from apple import Apple
from plant import Plant


class AppleTree(Plant):
    def __init__(self, *apples: Apple):
        self.apples = list(apples)

    def __repr__(self):
        return (f'{self.__class__.__name__ }('
                f'{self.apples!r}'
                f')')

    def grow(self):
        for apple in self.apples:
            apple.mature()

    def is_ripen(self) -> bool:
        return True if all(apple.is_ripen() for apple in self.apples) else False

    def collect_harvest(self) -> list[Apple]:
        harvest = self.apples
        self.apples = []
        return harvest
