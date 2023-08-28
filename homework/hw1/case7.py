# Функция на вход получает 2 переменные.
# a) Кол-во лет (int)
# b) Кол-во месяцев (int)
# Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.

def find_num_days(years: int = 0, month: int = 0) -> None:
    print((abs(years) * 12 + abs(month)) * 29)


find_num_days(month=1)
find_num_days(years=1)
find_num_days()
