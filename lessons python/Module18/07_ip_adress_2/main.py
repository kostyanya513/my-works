ip = input('Введите IP: ').split('.')
count = 0
if len(ip) != 4:
    print('Адрес - это четыре числа, разделенные точками.')
elif True:
    for index in range(len(ip)):
        if not ip[index].isdigit():
            print(ip[index], '- это не целое число')
        elif int(ip[index]) > 255:
            print(ip[index], 'превышает 255.')
        else:
            count += 1
if count == 4:
    print('IP-корректен')
