import random


class House:
    def __init__(self, holodilnik=50, tumb=0):
        self.holodilnik = holodilnik
        self.tumb = tumb

    def print_info_house(self):
        print('Еды в холодильнике: {}, Денег в тумбочке: {}'.format(
            self.holodilnik,
            self.tumb
        ))


class Person:
    def __init__(self, name, c_house):
        self.name = name
        self.house = c_house
        self.calm = 50

    def print_info(self):
        print('Имя: {}; Степень сытости: {}'.format(
            self.name, self.calm
        ))

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
            print('Жители умирают!')
            raise ValueError('Умирают')
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


house = House()
man_1 = Person('Федя', house)
man_2 = Person('Коля', house)

for _ in range(365):
    number_1 = random.randint(1, 6)
    number_2 = random.randint(1, 6)
    man_1.action(number_1)
    man_2.action(number_2)
man_1.print_info()
man_2.print_info()
house.print_info_house()
