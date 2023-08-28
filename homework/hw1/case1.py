# Напишите функцию которая возвращает длину принимаемой строки, по умолчанию строка пустая (s=’’). Пропишите все
# аннотации.

def get_string_length(string: str = '') -> int:
    return len(string)

print(get_string_length(string=''))
print(get_string_length(string='abc'))
print(get_string_length(string=' abc '))
print(get_string_length(string=r'\nlen'))
