class Stek:
    def __init__(self):
        self.m = []

    def put(self, c):
        return self.m.append(c)

    def pop(self):
        self.m.pop()


class TaskManager:
    """
    Класс Менеджер задач
    Attributes:
        d (dict): звдачи
    """
    def __init__(self):
        self.d = {}

    def new_task(self, a, b):
        """
        Метод добавления задачи в словарь задач
        :param a: (str) задача
        :param b: (int) приоритет
        """
        if b in self.d.keys():
            self.d[b].append(a)
        else:
            self.d[b] = [a]

    def __str__(self):
        """
        Магический метод вывода задач по приоритету: чем меньше число, тем выше задача
        k (int): ключ
        v (str): значение
        """
        sort = sorted(self.d.items())
        rez = ''
        for k, v in sort:
            rez += '{}: '.format(k) + '; '.join(v) + '\n'
        return 'Результат:\n{}'.format(rez)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
