import random


class Person:
    def __init__(self, name=None, calm=50, house=True):
        self.numb = None
        self.name = name
        self.calm = calm
        self.house = house

    def print_info(self):
        print('Имя: {}; Степень сытости: {}; Дом: {}'.format(
            self.name, self.calm, self.house
        ))

    def eat(self, numb):
        man.calm += numb
        home.fridge -= numb

    def work(self, numb):
        self.numb = numb
        man.calm -= numb
        home.money += numb

    def play(self, numb):
        man.calm -= numb

    def go(self, numb):
        home.fridge += numb
        home.money -= numb

    def action(self, numb):
        for day in range(365):
            if man.calm <= 0:
                man.house = False
                print('{} погибли от голода'.format(self.name))
            if man.calm < 20:
                man.eat(numb)
            elif home.fridge < 10:
                man.go(numb)
            elif home.money < 50:
                man.work(numb)
            elif numb == 1:
                man.work(numb)
            elif numb == 2:
                man.eat(numb)
            else:
                man.play(numb)


class House:
    def __init__(self, fridge=50, money=0):
        self.fridge = fridge
        self.money = money

    def print_info_house(self):
        print('Еды в холодильнике: {}, Денег в тумбочке: {}'.format(
            self.fridge,
            self.money
        ))


man = Person('Иван и Федя')
home = House()
for _ in range(365):
    number = 2 * random.randint(1, 6)
    man.action(number)
man.print_info()
home.print_info_house()
