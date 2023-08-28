number = 0

while number < 10:
    print(f'current ruble course: {number}')
    number += 1

string = 'jslkjkxk mlm'

while len(string) > 0:
    print('string existing - ' + string)
    string = string[:len(string)-1]
else:
    print('empty string')


def cycle_for(items: 'iterable') -> None:
    for item in items:
        print(item)


cycle_for('cycling')
cycle_for([1, 2, 3])
cycle_for(('a', 'b', 'c', 'd'))

numb_break = 0
while numb_break < 5:
    numb_break += 1
    if numb_break == 3:
        break
    print(f'number = {numb_break}')

numb_continue = 0
while numb_continue < 5:
    numb_continue += 1
    if numb_continue == 3:
        continue
    print(f'number = {numb_continue}')


try:
    print(a)
except:
    print('err')


try:
    print(a)
except Exception as ex:
    print('err')
    print(Exception)


try:
    print(k)
except ZeroDivisionError:
    k = 0
    print(k)
    print('app close')
finally:
    raise Exception('chto za ysas tyt tvoritsiy?!')