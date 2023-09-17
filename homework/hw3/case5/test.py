from apple import Apple
from apple_tree import AppleTree
from gardener import Gardener

apple_tree = AppleTree()

gardener = Gardener(
    'Михалыч',
    apple_tree,
)

for _ in range(10):
    gardener.get_statistics()
    print(gardener.take_harvest())
    gardener.take_care_of_plants()



