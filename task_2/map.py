
def square(number: int or float) -> int or float:
    return pow(number, 2)


numbers = [1, 2, 3, 4]
print(list(map(square, numbers)))
print(list(map(int, ['45', 8.2, 1])))

s = ' sfjhsjsf sdfsfklsl sfksjfls '
print(''.join(list(map(lambda letter: letter.upper(), filter(lambda letter: letter != ' ', s)))))


words = ['gdfgf', 'df', 'dsfsd', '']
print(list(map(len, words)))
