import numpy as np


def checkerboard(shape: tuple) -> np.ndarray:
    deck_template = np.zeros(shape)
    deck_template[1::2, ::2] = 1
    deck_template[::2, 1::2] = 1
    return deck_template


print(checkerboard(shape=(8, 7)))
