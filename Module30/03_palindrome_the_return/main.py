import collections


def can_be_poly(string: str) -> bool:
    res = collections.deque(string)  # возвращаем последовательность
    while len(res) > 1:  # цикл, проверяет уменьшение длины последовательности
        if collections.deque.popleft(res) != collections.deque.pop(res):  # сравниваем первый и последний удаленные # элементы последовательности
            return False
    return True


print(can_be_poly('abcba'))
print(can_be_poly('abbba'))
