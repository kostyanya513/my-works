import random
import string

i_list = [random.choice(string.ascii_letters) for _ in range(5)]
i_tuple = [random.randint(1, 10) for _ in range(5)]
i_tuple_2 = (random.randint(1, 10) for _ in range(5))

i_zip = zip(i_list, i_tuple)
print(i_zip)
for index in i_zip:
    print(index)

i_zip_2 = zip(i_list, i_tuple_2)
print(i_zip_2)
for index in i_zip_2:
    print(index)