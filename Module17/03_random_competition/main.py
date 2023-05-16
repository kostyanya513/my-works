import random
def change_team(i, j):
    if i >= j:
        return i
    else:
        return j

first_team = [random.randint(500, 1000) / 100 for i_first in range(20)]
second_team = [random.randint(500, 1000) / 100 for i_second in range(20)]
third_team = [change_team(first_team[i_third], second_team[i_third]) for i_third in range(20)]
print('Первая команда:', first_team)
print('Вторая команда:', second_team)
print('Победители тура:', third_team)
