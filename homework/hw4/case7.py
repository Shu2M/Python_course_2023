import numpy as np


def func(A: np.ndarray, S: int, last: bool = False):
    B = np.random.random((S, len(A)))
    C = np.dot(B, A)  # произведение матриц (S, X) * (X, 1) = (S, 1) то есть вектор
    # вопрос: о какой сумме каждой строки результирующей матрице идет речь?
    print(C)
    C = np.sin(C) if not last else np.maximum(C, 0)
    return C, B


c, _ = func(np.random.random(5), 10)
c, _ = func(c, 10)
c, _ = func(c, 5, last=True)
print(c * 100)

