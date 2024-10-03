line = list(input('Введите строку: '))
lline = []
lline.append(line[0])
count = 1
for index in line:
  if index != lline[-1]:
    lline.append(str(count))
    lline.append(index)
    count = 1
  else:
    count += 1
lline.append(str(count))
print(''.join(lline))