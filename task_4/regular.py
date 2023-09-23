import re

result = re.match(r'\d{2}', '123 - no string')
not_result = re.match(r'\d{2}', 'string')

print(result.group())
print(not_result)

result = re.search(r'\d{2}', 'string, 123 - no string')
print(result.group())

result = re.findall(r'\d{2}', 'string, 123 - no strin65g')
print(result)

result = re.fullmatch(r'\d{2}', '12')
print(result)


def is_mail(s: str) -> bool:
    return True if re.fullmatch(r'\w{3,}@\w{2,}\.\w{2,}', s) else False


print(is_mail('fsffs@lk.com'))
print(is_mail('fsffs@lk.c'))
