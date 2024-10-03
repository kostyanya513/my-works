list_films = []
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
quantity = int(input('Сколько фильмов хотите добавить?: '))

for i in range(quantity):
    film = input('Введите название фильма: ')
    if film in films:
        list_films.append(film)
    else:
        print('Ошибка: фильма', film, 'у нас нет :(')
print('Ваш список любимых фильмов:', list_films)