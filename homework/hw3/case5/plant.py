from abc import ABC, abstractmethod


class Plant(ABC):
    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def collect_harvest(self):
        pass

    @abstractmethod
    def is_ripen(self):
        pass
