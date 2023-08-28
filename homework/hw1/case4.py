# напишите функцию которая
# a) принимает число
# b) Если число больше 100 или меньше -100, то вывести в косоль символ “-”, иначе вывести на экран символ “+”

def is_number_in_range(number: int or float, min_number: int or float, max_number: int or float) -> None:
    print('-') if min_number > number or number > max_number else print('+')


is_number_in_range(number=1.12, min_number=-100, max_number=100)
is_number_in_range(number=-100.0, min_number=-100, max_number=100)
is_number_in_range(number=100.0, min_number=-100, max_number=100)
is_number_in_range(number=-100, min_number=-100, max_number=100)
is_number_in_range(number=100, min_number=-100, max_number=100)
is_number_in_range(number=100.12, min_number=-100, max_number=100)
