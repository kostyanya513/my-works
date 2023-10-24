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
        task_list (dict): звдачи
    """
    def __init__(self):
        self.task_list = {}

    def new_task(self, task, priority):
        """
        Метод добавления задачи в словарь задач
        :param task: (str) задача
        :param priority: (int) приоритет
        """
        if priority in self.task_list.keys():
            self.task_list[priority].append(task)
        else:
            self.task_list[priority] = [task]

    def __str__(self):
        """
        Магический метод вывода задач по приоритету: чем меньше число, тем выше задача
        key (int): ключ
        value (str): значение
        result (str): результат для вывода на экран
        """
        sort = sorted(self.task_list.items())
        result = ''
        for key, value in sort:
            result += '{}: '.format(key) + '; '.join(value) + '\n'
        return 'Результат:\n{}'.format(result)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
