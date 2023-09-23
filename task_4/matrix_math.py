import numpy as np

# a = np.arange(0, 4)
# b = np.arange(5, 9)
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a ** b)
#
# a = np.array([[1,2], [3,4], [5,6]])
# b = np.array([-1, 3])
# print(a+b)
# print(a*b)
#
# print(np.sqrt(a))
#
# print(a @ b)
# print(np.dot(a, b))
#
# data = np.genfromtxt('data.csv', delimiter=',')
# print(data)
# data = np.genfromtxt('data.txt', delimiter=',')
# print(data)
#
#
# def dot_mat(mat_shape_1: tuple, mat_shape_2: tuple) ->np.ndarray:
#     if mat_shape_1[1] == mat_shape_2[0]:
#         return np.dot(np.ones(mat_shape_1), np.ones(mat_shape_2))
#     else:
#         print(f"can't power matrixes with shapes {mat_shape_1} and {mat_shape_2}")
#         return None
#
#
# print(dot_mat((1, 3), (2, 1)))


def func():
    random_array = np.random.randint(15, size=15, dtype=int)
    print(random_array)
    random_array[(3 < random_array) & (random_array < 8)] *= -1

    # random_array = np.array(list(map(lambda x: -x if 3 < x < 8 else x, random_array)))
    return random_array


print(func())
