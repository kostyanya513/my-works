list_words = []
word = input('Введите слово: ')
list_words = list(word)
count = len(word)

for index in range(count // 2):
    if list_words[- index] == list_words[index - 1]:
        letter = True
    else:
        letter = False
        print('Слово не является палидромом')
        break
if letter:
    print('Слово является палиндромом')