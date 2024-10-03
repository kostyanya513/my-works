text = input('Введите строку: ')
word_list = text.split()
i = 0
while i != len(word_list):
    word = word_list[0]
    for i_word in word_list:
        if len(i_word) > len(word):
            word = i_word
    i += 1
print('Самое длинное слово:', word)
print('Длина этого слова:', len(word))
