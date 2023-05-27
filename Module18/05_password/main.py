password = input('Придумайте пароль: ')
uppers = len([letter for letter in password if letter.isupper()])
digins = len([number for number in password if number.isdigit()])
if len(password) < 8 or uppers < 0 or digins < 3:
    print('Пароль ненадежный! Попробуйте еще раз.')
else:
    print('Это надежный пароль!')
