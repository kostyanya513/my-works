# TODO здесь писать код
#while True:
ip = input('Введите IP: ')
iip = ip.split('.')
if ip.find(',') > 0:
    print('Адрес - это четыре числа, разделенные точками.')
elif True:
    for index in range(len(iip)):
        if not iip[index].isdigit():
            print(iip[index], '- это не целое число')
            break
        elif int(iip[index]) > 255:
            print(iip[index], 'превышает 255.')
            break
        else:
            print('IP-корректен')
