import re

numbers = 'А578АЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_pattern = r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
taxi_pattern = r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}'

list_private = re.findall(private_pattern, numbers)
list_taxi = re.findall(taxi_pattern, numbers)
print('Список номеров автомобилей:', list_private)
print('Список номеров такси:', list_taxi)
