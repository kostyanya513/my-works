quantity = int(input('Количество видеокарт: '))
list_videocard = []
new_list = []
maximum = 0

for i in range(quantity):
    print(i + 1, 'Видеокарта:', end = '')
    videocard = int(input())
    list_videocard.append(videocard)

for index in list_videocard:
    if index >= maximum:
        maximum = index

for index in list_videocard:
    if index != maximum:
        new_list.append(index)

print('Старый список видеокарт:', list_videocard)
print('Новый список видеокарт:', new_list)