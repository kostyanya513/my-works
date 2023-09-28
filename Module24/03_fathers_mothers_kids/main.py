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

    @staticmethod
    def eat_child(hunger):
        if hunger == 1:
            print('\nНужно покормить ребенка! {} {}!'.format(child.name, child.hungry[0]))

    @staticmethod
    def calm(calmness):
        if calmness == 1:
            print('\nНужно успокоить ребенка! {} {}!'.format(child.name, child.calmness[0]))

    @staticmethod
    def verification(age):
        if age - child.age > 16:
            return age
        else:
            raise ValueError('Ребенок должен быть старше родителя на 16 лет!')

    def print_info_parent(self):
        print('Меня зовут: {}\nМне: {}'.format(self.name, self.age))
        print('Мои дети:')
        for i_child in self.children:
            i_child.print_info_child()
            if i_child.ch_calm == 1:
                self.calm(i_child.ch_calm)
            if i_child.ch_hungry == 1:
                self.eat_child(i_child.ch_hungry)

    def add_child(self, next_child):
        if self.verification(self.age):
            self.children.append(next_child)


number_children = random.randint(1, 5)
man = Parent('Кот', 32)
for _ in range(number_children):
    calm = random.randint(0, 1)
    hungry = random.randint(0, 1)
    name_child = random.choice(string.ascii_uppercase)
    for index in range(5):
        name_child += random.choice(string.ascii_lowercase)
    age_child = random.randint(1, 16)
    child = Children(name_child, age_child, calm, hungry)
    man.add_child(child)
man.print_info_parent()

