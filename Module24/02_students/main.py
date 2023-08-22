class Student:
    def __init__(self, fi, group, usp):
        self.fi = fi
        self.group = group
        self.usp = usp

    def print_info(self):
        print('ФИ: {}\nГруппа: {}\nУспеваемость: {}\n'.format(
            self.fi,
            self.group,
            self.usp
        ))

    def __repr__(self):
        return repr((self.fi, self.group, self.usp))


students = [Student('Иванов Ваня', 1, [5, 4, 3, 2, 4]),
            Student('Петров Петя', 2, [5, 3, 4, 5, 3]),
            Student('Сидоров Кот', 3, [5, 5, 5, 5, 5]),
            Student('Спиридонов Андрей', 4, [4, 4, 4, 4, 4]),
            Student('Ермол Саня', 5, [3, 3, 3, 3, 3]),
            Student('Федоров Федя', 6, [2, 2, 3, 5, 4]),
            Student('Барчук Саня', 7, [5, 5, 2, 3, 3]),
            Student('Ильин Иль', 8, [4, 4, 4, 3, 3]),
            Student('Смирнов Капитон', 9, [3, 3, 3, 4, 4]),
            Student('Наумов Наум', 3, [5, 3, 2, 4, 5])]

list_student = sorted(students, key=lambda student: (sum(student.usp)) / 5)
for i_student in list_student:
    i_student.print_info()
