double = lambda x: x*2
print(double(2))

list_values = [i for i in range(11)]
print(list(filter(lambda x: x % 2 == 0, list_values)))


sentence = 'ddfdf dfddf dfd'
print(list(filter(lambda sym: sym != ' ', sentence)))

lst = [1, 2, 2.6, [4, 8], 'fdf', {}, (4, 8)]
print(list(filter(lambda e: isinstance(e, int), lst)))


def filter_num(in_num):
    return in_num % 2 == 0


list_values = [i for i in range(11)]
print(list(filter(filter_num, list_values)))



























