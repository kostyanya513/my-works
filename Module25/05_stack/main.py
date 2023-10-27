class Stack:
    """
    Класс Stack
    Atributes:
    dict_task (dict) список задач
    """

    def __init__(self):
        self.dict_task = []

    def __str__(self):
        return str('; '.join(self.dict_task))

    def put(self, element):
        """
        Метод добавления задачи в стек
        """
        self.dict_task.append(element)

    def pop(self):
        """
        Метод удаления задачи из стека
        """
        if len(self.dict_task) == 0:
            return None
        return self.dict_task.pop()


class TaskManager:
    """
    Класс Менеджер задач
    Attributes:
        task_list (dict): задачи
    """

    def __init__(self):
        self.task_list = {}

    def new_task(self, task, priority):
        """
        Метод добавления задачи в стек, если уже есть задачи с таким приоритетом.
        Или добавляется стек и одна задача в него.
        """
        if priority in self.task_list.keys():
            new_task = Stack()
            while len(str(self.task_list[priority])) != 0:
                value = self.task_list[priority].pop()
                if value != task:
                    new_task.put(value)
            new_task.put(task)
            self.task_list[priority] = new_task
        else:
            self.task_list[priority] = Stack()
            self.task_list[priority].put(task)

    def delete_task(self, priority):
        """
        Метод удаления задачи из стека, если такая имеется
        :param priority: (int) приоритет
        """
        if priority in self.task_list.keys():
            print('Удалили задачу {}'.format(self.task_list[priority].pop()))
            if len(str(self.task_list[priority])) == 0:
                self.task_list.pop(priority)
        else:
            print('Задача с данным приоритетом отсутствует!')

    def __str__(self):
        """
        Магический метод вывода задач по приоритету: чем меньше число, тем выше задача
        key (int): ключ
        result (str): результат для вывода на экран
        """
        result = ''
        for key in sorted(self.task_list.keys()):
            result += str(key) + ' ' + str(self.task_list[key]) + '\n'
        return 'Результат:\n{}'.format(result)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.delete_task(2)
print(manager)
