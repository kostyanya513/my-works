import collections

# вводится строка
message = "Today is a beautiful day! The sun is shining and the birds are singing."

# считается количество уникальных элементовэлементов
unique_count = len(list(filter(lambda elem: elem[1] == 1, collections.Counter(message).most_common()[::-1])))

# выводится количество уникальных элементов
print("Количество уникальных символов в строке:", unique_count)
