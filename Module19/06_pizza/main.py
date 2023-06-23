number = int(input('Введите количество заказов: '))
all_zakaz = dict()
for index in range(number):
  zakaz = input(f'{index + 1}-й заказ: ').split()
  if not zakaz[0] in all_zakaz:
    all_zakaz[zakaz[0]] = {zakaz[1]:int(zakaz[2])
    }
  else:
    if not zakaz[1] in all_zakaz[zakaz[0]]:
      all_zakaz[zakaz[0]][zakaz[1]] = int(zakaz[2])
    else:
      all_zakaz[zakaz[0]][zakaz[1]] += int(zakaz[2])
for index in all_zakaz:
  print(f'{index}:')
  for pizza in all_zakaz[index]:
    print(f'{pizza}: {all_zakaz[index][pizza]}')
