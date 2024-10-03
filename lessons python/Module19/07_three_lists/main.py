array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

variety_1 = set(array_1)
variety_2 = set(array_2)
variety_3 = set(array_3)
common_element_1 = variety_1 & variety_2 & variety_3
print('Решение с множествами:', common_element_1)
different_elements_1 = variety_1 - (variety_2 | variety_3)
print('Решение с множествами:', different_elements_1)

common_element_2 = []
different_elements_2 = []
for a in array_1:
  if a in array_2 and a in array_3:
    common_element_2.append(a)
  elif a not in array_2:
    if a not in array_3:
      different_elements_2.append(a)
print('Решение без множеств:', common_element_2)
print('Решение без множеств:', different_elements_2)

