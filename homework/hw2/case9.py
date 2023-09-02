from time import perf_counter


def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        status, result = func(*args, **kwargs)
        end_time = perf_counter()
        print(f"Время работы функции {result}: \t", end_time - start_time, " сек")
    return wrapper


@execution_time_decorator
def test_func_1():
    for i in range(10000):
        pass
    return True, 'test_func_1'


@execution_time_decorator
def test_func_2():
    a = [i for i in range(10000)]
    for i in a:
        pass
    return True, 'test_func_2'


test_func_1()
test_func_2()
