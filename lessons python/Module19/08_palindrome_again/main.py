text = input('Введите строку: ')
summ = 0
letters = {}
for letter in text:
  if letter in letters:
    letters[letter] += 1
  else:
    letters[letter] = 1
for letter in letters:
  if letters[letter] % 2 > 0:
    summ += 1

if summ > 1:
  print('Нельзя сделать палиндромом')
else:
  print('Можно сделать палиндромом')
