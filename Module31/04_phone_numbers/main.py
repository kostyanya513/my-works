import re

numbers = ['9999999999', '999999-999', '99999x9999']
number_pattern = r'[8,9]\d{9}'


for number in numbers:
    res = re.search(number_pattern, number)
    print(bool(res))
