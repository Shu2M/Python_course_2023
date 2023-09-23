import numpy as np


def get_possible_shapes(number: int) -> list[tuple]:
    possible_shapes = list()
    for n in range(2, number):
        if not number % n:
            possible_shapes.append((n,  number // n))

    if not possible_shapes:
        print(f'Число {number} нельзя разбить на множители без остатка')

    return possible_shapes[:len(possible_shapes) // 2]


def create_possible_matrices(number_of_elements: int) -> list[np.ndarray]:
    possible_matrices = list()
    shapes = get_possible_shapes(number_of_elements)
    for shape in shapes:
        possible_matrices.append(np.random.random(shape))
    return possible_matrices


number_of_elements = 3
matrices = create_possible_matrices(number_of_elements)
for matrix in matrices:
    print(matrix, '\n')
