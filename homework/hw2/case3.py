def find_str(*args) -> tuple:
    return tuple(filter(lambda x: isinstance(x, str), args))


print(find_str(54, 65, 87, 'gf', 'fg'))
