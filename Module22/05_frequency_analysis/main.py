alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z')
text_file = open('text.txt', 'r')
data = text_file.read().lower().split()
list_data = ''.join(data)
quantity = {}
for letter in list_data:
    if letter in alphabet:
        quantity.setdefault(letter, 0)
        quantity[letter] += 1 / len(list_data)
sorted_quantity = {key: value for key, value in sorted(quantity.items(), key=lambda item: (-item[1], item[0]))}
text_file.close()

analysis_file = open('analysis.txt', 'w')
for key, value in sorted_quantity.items():
    gistograma = analysis_file.write(key + ' ' + str(round(value, 3)) + '\n')
analysis_file.close()
