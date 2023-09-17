from apple import Apple
from apple_tree import AppleTree
from gardener import Gardener

apple_1 = Apple()
apple_2 = Apple()
apple_3 = Apple()
apple_4 = Apple()
apple_5 = Apple()

apple_tree = AppleTree(
    apple_1,
    apple_2,
    apple_3,
    apple_4,
    apple_5,
)

gardener = Gardener(
    'Михалыч',
    apple_tree,
)

gardener.take_harvest()
gardener.take_care_of_plants()
gardener.take_harvest()
gardener.take_care_of_plants()
print(gardener.take_harvest())

