import random


class Warrior:

    def __init__(self, health=100, viktory=False):
        self.health = health
        self.viktory = viktory

    def loss_health(self, user):
        self.health -= 20
        print('Здоровье {} игрока: {}'.format(user, self.health))
        if self.health == 0:
            return True

    def info(self, n=0):
        print('Здоровье {} игрока: {}'.format(n, self.health))


warrior_first = Warrior()
warrior_second = Warrior()
warrior_first.info(1)
warrior_second.info(2)
for i in range(20):
    number = random.randint(1, 2)
    if number == 1:
        if warrior_first.loss_health(number):
            print('Победа 2 игрока')
            break
    else:
        if warrior_second.loss_health(number):
            print('Победа 1 игрока')
            break
