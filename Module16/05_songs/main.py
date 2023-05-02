violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

total_time = 0
number = int(input('Сколько песен выбрать? '))
for i_songs in range(number):
    print('Название', i_songs + 1, end= '')
    print('-й песни:', end= ' ')
    song = input()
    for index in range(len(violator_songs)):
        if song == violator_songs[index][0]:
            total_time += violator_songs[index][1]
print('Общее время звучания песен:', round(total_time, 2))