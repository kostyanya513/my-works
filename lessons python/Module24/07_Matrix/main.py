class Matrix:
    def __init__(self, strok, stolbec):
        self.strok = strok
        self.stolbec = stolbec
        self.data = [[0 for _ in range(stolbec)] for _ in range(strok)]

    def add(self, other):
        if self.strok != other.strok or self.stolbec != other.stolbec:
            raise ValueError('Матрицы должны быть одинаковы')
        result = Matrix(self.strok, self.stolbec)
        for i in range(self.strok):
            for j in range(self.stolbec):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def subtract(self, other):
        if self.strok != other.strok or self.stolbec != other.stolbec:
            raise ValueError('Матрицы должны быть одинаковы')
        result = Matrix(self.strok, self.stolbec)
        for i in range(self.strok):
            for j in range(self.stolbec):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def multiply(self, other):
        if self.stolbec != other.strok:
            raise ValueError('Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы!')
        result = Matrix(self.strok, other.stolbec)
        for i in range(self.strok):
            for j in range(other.stolbec):
                for k in range(self.stolbec):
                    result.data[i][j] = self.data[i][k] * other.data[k][j]
        return result

    def transpose(self):
        result = Matrix(self.stolbec, self.strok)
        for i in range(self.strok):
            for j in range(self.stolbec):
                result.data[j][i] = self.data[i][j]
        return result

    def __str__(self):
        output = ''
        for stroc in self.data:
            output += '\t'.join(str(element) for element in stroc)
            output += '\n'
        return output


# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

print('Вывод:')
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
print("Матрица 3:")
m3.data = [[1, 2], [3, 4], [5, 6]]
print(m3)

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
