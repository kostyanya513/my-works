import random
import string


class Children:
    calmness = {0: 'Спокоен', 1: 'Плачет'}
    hungry = {0: 'Сыт', 1: 'Голоден'}

    def __init__(self, name, age, ch_calm, ch_hungry):
        self.name = name
        self.age = age
        self.ch_calm = ch_calm
        self.ch_hungry = ch_hungry

    def print_info_child(self):
        print('\n\tИмя ребенка: {}\n\tВозраст ребенка: {}\n\tСостояние спокойствия: {}\n\tСостояние голода: {}'.format(
            self.name, self.age, self.calmness[self.ch_calm], self.hungry[self.ch_hungry]
        ))


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def print_info_parent(self):
        print('\nМеня зовут: {}\nМне: {}'.format(self.name, self.age))
        print('Мои дети:')
        for i_child in self.children:
            i_child.print_info_child()

    def verification_calm(self, child):
        if child.ch_calm == 1:
            print('\n{} нужно успокоить!'.format(child.name))
            child.ch_calm = 0

    def verification_hungry(self, child):
        if child.ch_hungry == 1:
            print('\n{} нужно покормить!'.format(child.name))
            child.ch_hungry = 0

    def add_child(self, next_child):
        self.children.append(next_child)


number_children = random.randint(1, 5)
man = Parent('Кот', 32)

calm_1 = random.randint(0, 1)
hungry_1 = random.randint(0, 1)
child_1 = Children(random.choice(string.ascii_letters), random.randint(1, 15), calm_1, hungry_1)
man.add_child(child_1)

calm_2 = random.randint(0, 1)
hungry_2 = random.randint(0, 1)
child_2 = Children(random.choice(string.ascii_letters), random.randint(1, 15), calm_2, hungry_2)
man.add_child(child_2)

man.print_info_parent()
if calm_1 or hungry_1:
    man.verification_calm(child_1)
    man.verification_hungry(child_1)
    child_1.print_info_child()
if calm_2 or hungry_2:
    man.verification_calm(child_2)
    man.verification_hungry(child_2)
    child_2.print_info_child()
