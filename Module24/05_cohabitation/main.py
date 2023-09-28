import random


class House:
    def __init__(self, holodilnik=50, tumb=0):
        self.holodilnik = holodilnik
        self.tumb = tumb

    def print_info_house(self):
        print('  : {},   : {}'.format(
            self.holodilnik,
            self.tumb
        ))


class Person:
    def __init__(self, name, calm=50):
        self.name = name
        self.calm = calm
        self.house = House()

    def print_info(self):
        print(': {};  : {}'.format(
            self.name, self.calm
        ))
        self.house.print_info_house()

    def eat(self, number):
        self.calm += number
        self.house.holodilnik -= number

    def work(self, number):
        self.calm -= number
        self.house.tumb += number

    def play(self, number):
        self.calm -= number

    def go_shop(self, number):
        self.house.holodilnik += number
        self.house.tumb -= number

    def action(self, number):
        if self.calm <= 0:
            print(' !')
            raise ValueError('')
        if self.calm < 20:
            self.eat(number)
        elif self.house.holodilnik < 10:
            self.go_shop(number)
        elif self.house.tumb < 50:
            self.work(number)
        elif number == 1:
            self.work(number)
        elif number == 2:
            self.eat(number)
        else:
            self.play(number)


man_1 = Person('')
man_2 = Person('')
house = House()
for _ in range(365):
    number_1 = random.randint(1, 6)
    number_2 = random.randint(1, 6)
    man_1.action(number_1)
    man_2.action(number_2)
man_1.print_info()
man_2.print_info()
