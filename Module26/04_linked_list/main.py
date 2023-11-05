class Node:
    def __init__(self, n):
        self.n = n
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0

    def __len__(self):
        return self.len

    def append(self, num):
        self.len += 1
        if self.first is None:
            self.last = self.first = Node(num)
        else:
            self.last.next = self.last = Node(num)

    def get(self, num):
        if self.len < num:
            return 'Такого элемента нет!'
        curr = self.first
        c = 0
        while curr is not None:
            c += 1
            if c == num:
                return curr.n
            curr = curr.next

    def remove(self, num):
        if self.len < num:
            return 'Такого элемента нет!'
        curr = self.first
        c = 0
        old = None
        while curr is not None:
            if c == num:
                if curr.next is None:
                    self.last = curr
                old.next = curr.next
                break
            old = curr
            curr = curr.next
            c += 1

    def __str__(self):
        if self.first != 0:
            current = self.first
            out = '[ ' + str(current.n) + ' '
            while current.next is not None:
                current = current.next
                out += str(current.n) + ' '
            return out + ']'
        return 'Текущий список: []'


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(3))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
