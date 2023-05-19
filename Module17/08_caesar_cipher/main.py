alphavit = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
     'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
     'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
word = list(input('Введите сообщение: '))
shift = int(input('Введите сдвиг: '))
new = [(alphavit[(alphavit.index(variable) + shift) % 33] if variable in alphavit else ' ')
       for variable in word]
print('Зашифрованное слово:',new)