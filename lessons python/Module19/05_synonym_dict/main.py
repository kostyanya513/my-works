number = int(input('Введите количество пар слов: '))
list = dict()
list1 = dict()
for index in range(number):
  print(f'{index +1} пара:', end=' ')
  list_pair = input().lower().split(' - ')
  list[list_pair[0]] = list_pair[1]
  list1[list_pair[1]] = list_pair[0]
print(list)
print(list1)
word = input('Введите слово: ').lower()
if word in list:
  print('Синоним:', list[word])
elif word in list1:
  print('Синоним:', list1[word])
else:
  print('нет')
