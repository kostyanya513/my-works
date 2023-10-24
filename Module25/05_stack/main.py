class Stek:
    def __init__(self):
        self.m = []

    def put(self, c):
        return self.m.append(c)

    def pop(self):
        self.m.pop()


class TaskManager:
    def __init__(self):
        self.d = {}

    def new_task(self, a, b):
        if b in self.d.keys():
            self.d[b].append(a)
        else:
            self.d[b] = [a]

    def __str__(self):
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
