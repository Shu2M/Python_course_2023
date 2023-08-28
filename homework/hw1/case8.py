# Напишите функцию которая
# a) на вход получает строковую переменную.
#   i) в строке содержится несколько слов
# b) Возвращает строку состоящую из аббревиатур слов переменной.
# c) Если на вход поступил другой тип данных, должно срабатывать исключение
# d) Результат работы функции распечатайте в консоль
import re


def get_abbreviation(string_with_words: str) -> None:
    try:
        print(''.join(map(lambda x: x[0].upper(), re.findall(r'\b\w{2,}\b', string_with_words))))
    except Exception as ex:
        print(f'Исключение: {ex}')


get_abbreviation(string_with_words="Python,Java,Perl,PHP,Swift")
get_abbreviation(string_with_words="Я\nучу; язык,программирования\nPython")
get_abbreviation(string_with_words=4)