age = 21
print('age: ', age)

count = 15
print('count: ', count)

print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)
print(2 // 2)
print(2 % 2)
print(2 ** 2)

s = ' this is string'
s1 = '''this
is 
big
string'''
print(s + '\n')
print(s1 + '\n')

print('sum ' + 'string')
print('power'*3)
print(len('len'))

a = 'auto'
print(a[0])
print(a[0:2])
print(a[-1])
print(a.index('t'))

a = [1, 2, 2]
b = ['sd', [1.1, 4, 5], 32]
c = ['fd', 'df', 'def']

print('a[2] = ', a[2])
print('a[0:2] = ', a[0:2])

a[2] = 4
print(a)

for el in a:
    print(el)

print(len(a))
a.append('f')
print(a)

print(10 < 0)
print(10 > 0)
print(10 <= 0)
print(10 >= 0)
print(10 == 0)
print(10 != 0)

a = True
if a:
    print('a = True')
else:
    print('a = False')