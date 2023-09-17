from plant import Plant


class Gardener:
    def __init__(
            self,
            name: str = 'unknown',
            *plants: Plant,
    ):
        self.name = name
        self.tracked_plants = plants

    def take_care_of_plants(self):
        for plant in self.tracked_plants:
            plant.grow()

    def take_harvest(self):
        basket = []
        for plant in self.tracked_plants:
            basket.append(plant.collect_harvest())
        return basket

    def get_statistics(self):
        for plant in self.tracked_plants:
            print(plant)
