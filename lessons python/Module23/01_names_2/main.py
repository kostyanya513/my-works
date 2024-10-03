def check_len_string(number, string):
    try:
        if len(number.strip()) < 3:
            raise Exception
    except Exception:
        print('Длина {} строки меньше трех символов'.format(string))
        with open('errors.log', 'a', encoding='utf-8') as errors_file:
            errors_file.write('Длина {} строки меньше трех символов\n'.format(string))
        return 0
    return len(number)


summ_number_name = 0
len_string = 0
with open('people.txt', 'r', encoding='utf-8') as names:
    for name in names:
        len_string += 1
        summ_number_name += check_len_string(name.strip(), len_string)
print(summ_number_name)
