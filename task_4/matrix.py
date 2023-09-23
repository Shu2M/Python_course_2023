import numpy as np
from typing import Any
import random

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(a)
print(a[1, 2])

print(a.shape)
print(a.dtype)

b = np.array(range(10), float)
b_reshape = b.reshape((2, 5))
print(b)
print(b_reshape)

print(b.tolist())


def sort_args(*args: Any) -> np.ndarray:
    return np.array(sorted(filter(lambda arg: isinstance(arg, int), args)))


a = sort_args(1,4,20.6,0,-45,-6, list, dict, object, True, False, 1.0, '1', '1.0')
print(a)
print(type(a))


def create_2d_array(x: int, y: int) -> np.ndarray:
    return np.array([[random.random() for _ in range(x)] for _ in range(y)])


def calc_min_max_mean(two_d_array: np.ndarray) -> tuple:
    return two_d_array.min(), two_d_array.max(), two_d_array.mean()


print(calc_min_max_mean(create_2d_array(4, 5)))
print(np.random.sample())

a = np.array(range(6), float).reshape((2, 3))
print(a)
print()
print(a.T)
print(a.flatten())
print(a.T.flatten())

a = np.arange(0, 3)
b = np.arange(4, 9)
c = np.arange(7, 12)
print(np.concatenate((a, b, c)))

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(np.concatenate((a, b)))
print(np.concatenate((a, b), axis=0))
print(np.concatenate((a, b), axis=1))

app = np.array(range(10), int)
print(app)
app_new = np.append(app, 10)
print(app_new)

app = np.array([[1, 2], [3, 4]])
print(app)
app_new = np.append(app, np.array([[10, 11]]), axis=0)
print(app_new)