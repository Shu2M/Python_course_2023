def not_int_exception(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            return result
        else:
            raise Exception('Тип выводимых данных не int')
    return wrapper


@not_int_exception
def f_1():
    return 1


@not_int_exception
def f_2():
    return 0.1


f_1()
f_2()
