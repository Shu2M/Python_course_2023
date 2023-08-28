# Напишите функцию для нахождения факториала числа.

def calc_factorial(number: int) -> int:
    p = 1
    for num in range(1, number+1):
        p *= num
    return p


print(calc_factorial(6))
print(calc_factorial(0))
print(calc_factorial(1))
