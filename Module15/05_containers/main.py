list_containers = []
count = 1
quantity = int(input('Количество контейнеров: '))
for index in range(quantity):
    weight = int(input('Введите вес контейнера: '))
    if weight >= 200:
        print('Вес не должен превышать 200')
    else:
        list_containers.append(weight)

new_container = int(input('Введите вес нового контейнера: '))
for index in list_containers:
    if new_container <= index:
        count += 1
print('Номер, который получит новый контейнер:', count)