def all_letters(list_text):
  all_letter = dict()
  for i in list_text:
    if i in all_letter:
      all_letter[i] += 1
    else:
      all_letter[i] = 1
  return all_letter

text = input('Введите текст: ').lower()
list = all_letters(text)
print('Оригинальный словарь частот:')
for index, znach in sorted(list.items()):
  print(index, ':', znach)
schetchik = dict()

print()
print('Инвертированный словарь частот:')
for index in list:
  if not list[index] in schetchik:
    schetchik[list[index]] = []
for index in schetchik:
  for i in list:
    if index == list[i]:
      schetchik[index].append(i)
  print(index, ':', schetchik[index])
