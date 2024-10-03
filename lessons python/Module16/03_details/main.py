shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

count_detail = 0
summ = 0

detail = input('Название детали: ')
for i in range(len(shop)):
        if detail == shop[i][0]:
                count_detail += 1
                summ += shop[i][1]
print('Количество деталей -', count_detail)
print('Общая стоимость -', summ)

