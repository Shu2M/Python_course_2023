lang = 'python'

if lang == 'python':
    print('hello')
print('end')


def get_type_of_sentence(sentence: str = '') -> str:
    if sentence:
        last = sentence[-1]

        if last == '?':
            sentence_type = 'question'
        else:
            sentence_type = 'normal'
    else:
        sentence_type = 'empty sentence'

    return sentence_type


def user_number(user_data: int or float) -> None:
    permit_print = True

    if permit_print and user_data == -6:
        print('number -6')
    elif permit_print and user_data > 0:
        print('positive number')
    elif not permit_print:
        print('printing access denied')


user_number(-6)
user_number(10)
user_number(-5)

print(get_type_of_sentence('sentence'))
print(get_type_of_sentence('sentence?'))
print(get_type_of_sentence(''))


def get_course_name(course_number: int) -> None:
    if course_number in range(1, 5):
        print('bakalavr')
    elif course_number in range(5, 7):
        print('magistr')
    elif course_number in range(6, 10):
        print('aspirant')
    else:
        print('vvedite correctniy god obuchenia')


get_course_name(3.5)
