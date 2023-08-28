# Напишите функцию которая отвечает “ДА” или “НЕТ” на вопрос в комментарие.
# str_2 содержит в себе str_1?

def is_str1_in_str2(str_1: str, str_2: str) -> None:
    if str_1 in str_2:
        print('ДА')
    else:
        print('НЕТ')

is_str1_in_str2(str_1='test', str_2='test1')
is_str1_in_str2(str_1='test1', str_2='test1')
is_str1_in_str2(str_1='test1212', str_2='test1')
is_str1_in_str2(str_1='test21', str_2='test1')
is_str1_in_str2(str_1='', str_2='')
