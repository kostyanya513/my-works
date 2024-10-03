import math


class MyMath:
    """
    Класс для вычмсления размеров геометрических фигур
    Args:
        radius (int): передается радиус
        length (int): передается длина
    Attributs:
        pi (float) - число ПИ
    """
    pi = math.pi

    def __init__(self, radius: int, length: int) -> None:
        self.__length = length
        self.__radius = radius

    @classmethod
    def circle_len(cls, radius: int) -> float:
        """
        Метод для вычисления длины окружности
        :return: длина окружности
        :rtype: float
        """
        return 2 * MyMath.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        """
        Метод для вычисления площади окружности
        :return: площадь окружности
        :rtype: float
        """
        return MyMath.pi * radius ** 2

    @classmethod
    def volume_cube(cls, length: int) -> float:
        """
        Метод для вычисления объема куба
        :return: объем куба
        :rtype: float
        """
        return length ** 3

    @classmethod
    def area_sphere(cls, length: int) -> float:
        """
        Метод для вычисления площади поверхности сферы
        :return: площадь поверхности сферы
        :rtype: float
        """
        return 4 * MyMath.pi * length ** 2

    @property
    def radius(self) -> int:
        """
        Геттер для получения радиуса
        :return: __radius
        :rtype: int
        """
        return self.__radius

    @radius.setter
    def radius(self, radius: int) -> None:
        """
        Сеттер для установления радиуса
        :param radius: радиус
        :rtype: int
        """
        self.__radius = radius

    @property
    def length(self) -> int:
        """
        Геттер для получения длины
        :return: __lenght
        :rtype: int
        """
        return self.__length

    @length.setter
    def length(self, length: int) -> None:
        """
        Cеттер для кстановления длины
        :param length: длина
        :rtype: int
        """
        self.__length = length


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
