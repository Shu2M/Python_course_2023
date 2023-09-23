import numpy as np
import array

a = np.array([1, 2, 3, 4])
print(type(a))

print(a[:2])
print(a[1])

a[0] = 10.1
print(a)

b = np.full(10, 1)
print(b)

b = a[::-1]
print(a)

x = np.zeros(10)
print(x)

x = np.ones(10)
print(x)

x = np.full(10, 3.7)
print(x)

x = np.arange(10, 20)
print(x)

print(x.mean())
print(x.max())
print(x.min())