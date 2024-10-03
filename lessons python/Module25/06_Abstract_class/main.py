import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Абстрактный класс
    Attrubuts:
    s (int): площадь фигуры
    """
    def __init__(self):
        self.s = None

    @abstractmethod
    def area(self):
        pass

    def print_area(self):
        """
        Метод вывода на экран площади фигуры
        """
        return self.s


class Circle(Shape):
    """
    Класс Круг. Родитель: Shape
    Args:
        r (int): радиус круга
    """
    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        """
        Переопределенный метод для расчета плащади круга
        """
        self.s = math.pi * self.r * 2


class Rectangle(Shape):
    """
    Класс Прямоугольник. Родитель: Shape
    Args:
        a (int): длина прямоугольника
        b (int): ширина прямоугольника
    """
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        """
        Переопределенный метод для расчета плащади прямоугольника
        """
        self.s = self.a * self.b


class Triangle(Shape):
    """
    Класс Треугольник. Родитель: Shape
    Args:
        a (int): длина основания
        b (int): высота треугольника
    """
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        """
        Переопределенный метод для расчета плащади треугольника
        """
        self.s = self.a * self.b / 2


# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площади фигур
circle.area()
rectangle.area()
triangle.area()

# Вывод результатов
print("Площадь круга:", circle.print_area())
print("Площадь прямоугольника:", rectangle.print_area())
print("Площадь треугольника:", triangle.print_area())
