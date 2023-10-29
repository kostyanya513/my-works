from collections.abc import Iterable


class Genclass:
    def __init__(self, num: int) -> None:
        self.num = num
        self.next = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.next < self.num:
            self.next += 1
            return self.next ** 2
        else:
            raise StopIteration


def generate(n: int) -> Iterable[int]:
    g = 1
    for _ in range(1, n + 1):
        yield g ** 2
        g += 1


number = int(input('Введите число: '))

sequence = [x ** 2 for x in range(1, number + 1)]
print('Генераторное выражение: \t', end='')
for index in sequence:
    print(index, end=' ')

print('\nФункция генератор: \t', end='')
for i in generate(number):
    print(i, end=' ')

print('\nКласс-итератор: \t', end='')
gen_class = Genclass(number)
for i in gen_class:
    print(i, end=' ')
