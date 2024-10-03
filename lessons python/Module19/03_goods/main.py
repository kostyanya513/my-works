import math

def all_costs(product):
    cost_goods = dict()
    for y in product:
        cost_goods['prod'] = product[y]
        break
    cost_goods['summa_za_vd'] = math.prod(dict.values(product))
    return cost_goods

def funkciya(string):
    tovar = dict()
    product_in_stock = []
    products_stock = []
    for i in string:
        all_costs(i)
        product_in_stock.append(all_costs(i))
    for d in product_in_stock:
        for k in d.keys():
            tovar[k] = tovar.get(k, 0) + d[k]
    products_stock.append(tovar)
    return products_stock

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for index in store:
  store[index] = funkciya(store[index])

for index in goods:
  p = store[goods[index]][0]['prod']
  s = store[goods[index]][0]['summa_za_vd']
  print(f'{index} - {p} штук, стоимость {s} рублей')
