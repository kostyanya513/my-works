class Parent:
    name = 'Константин'
    age = 38
    children = ''

    def print_info(self):
        print('Имя родителя: {}\nВозраст: {}\nСписок детей:  {}'.format(
            self.name, self.age, self.children
        ))

    def eat_child(self):
        if child.hungry == True:
            child.hungry = False
            print('\nПоел!')
            child.print_info_child()

    def calm(self):
        if child.calm == False:
            child.calm = True
            print('\nСпокоен!')
            child.print_info_child()


class Children:

    def __init__(self, name, age, calm, hungry):
        self.name = name
        self.age = age
        self.calm = calm
        self.hungry = hungry

    def print_info_child(self):
        print('\nИмя ребенка: {}\nВозраст ребенка: {}\nСостояние спокойствия: {}\nСостояние голода: {}'.format(
            self.name, self.age, self.calm, self.hungry
        ))


parent = Parent()
child = Children('Валерий', 15, False, True)
parent.print_info()
child.print_info_child()
parent.calm()
parent.eat_child()
