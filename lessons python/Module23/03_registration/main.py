def user_verification(user_string):
    try:
        if len(user_string) < 3:
            raise IndexError
        elif str(user_string).isalpha():
            raise NameError
        elif not '@' and '.' in list(user_string[1]):
            raise SyntaxError
        elif not 10 <= int(user_string[2]) < 99:
            raise ValueError
        else:
            user_good.write(' '.join(user_string) + '\n')
    except IndexError:
        user_bad.write(' '.join(user_string) + '\t\tНЕ присутствуют все три поля!\n')
    except NameError:
        user_bad.write(' '.join(user_string) + '\t\tПоле «Имя» содержит НЕ только буквы!\n')
    except SyntaxError:
        user_bad.write(' '.join(user_string) + '\t\tПоле «Имейл» НЕ содержит @ и . (точку)!\n')
    except ValueError:
        user_bad.write(' '.join(user_string) + '\t\tПоле «Возраст» НЕ является числом от 10 до 99!\n')


user = open('registrations.txt', 'r', encoding='utf-8')
user_good = open('registrations_good.log', 'w', encoding='utf-8')
user_bad = open('registrations_bad.log', 'w', encoding='utf-8')
for user_data in user:
    i_user = user_data.strip().split()
    user_verification(i_user)
user_bad.close()
user_good.close()
user.close()
