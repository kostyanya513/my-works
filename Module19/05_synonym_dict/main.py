number = int(input('Введите количество пар слов: '))
list_pair = [input(f'{index + 1} парa: '.lower()).split(' - ')
             for index in range(number)]
summ = 0
word = input('Введите слово: ')
for index in list_pair:
  if word == index[0]:
    print('Синоним:', index[1])
    break
  elif word == index[1]:
    print('Синоним:', index[0])
    break
  else:
    summ += 1
if summ == number:
  print('Такого слова нет в слова в словаре.')
