def try_again(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print('Первый запуск функции прошел успешно')
        except Exception:
            print('Первый запуск провалился, пробуем снова...')
            func(*args, **kwargs)
    return wrapper


@try_again
def f_1():
    return 1/0


@try_again
def f_2():
    return 1/1


f_2()
f_1()
