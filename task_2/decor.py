def currency(fn):
    def wrapper(*args, **kwargs):
        price = fn(*args, **kwargs)
        return f'{price} руб'
    return wrapper


@currency
def price_calculation(price, tax):
    return price * (1 + tax)


def result_output(fn):
    def wrapper(*args, **kwargs):
        result, msg = fn(*args, **kwargs)[0], fn(*args, **kwargs)[1] or "Результат вычисления"
        return f'{msg}: {result}'
    return wrapper


@result_output
def square(n):
    return pow(n, 2), f'Результат возведения {n} в степень 2'


@result_output
def power2(n):
    return n * 2, f'Результат умножения {n} на 2'


@result_output
def power3(n):
    return n * 3, ''


print(square(165))
print(power2(13))
print(power3(3))





















