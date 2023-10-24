class Property:
    """
    Базовый класс, описывающий стоимость имущества
    Args:
        worth (int): передается стоимость имущества
        cost (int): передается количество денег
    Attributes:
        taxe (int): надог на имущество
    """
    def __init__(self, worth, cost):
        self.worth = worth
        self.cost = cost
        self.taxe = 0

    def calculation(self):
        """
        Метод расчета налога и количества недостающих денег

        """
        if self.cost - self.taxe >= 0:
            print('Налог {}'.format(self.taxe))
        elif self.cost - self.taxe < 0:
            print('Налог {}, не хватает {}'.format(
                self.taxe, (self.cost - self.taxe))
            )


class Apartment(Property):
    """
    Класс квартира. Родитель: Property
    Args:
        worth (int): передается стоимость квартиры
        cost (int): передается количество денег
    Attributes:
        taxe (int): расчет надога на квартиру
    """
    def __init__(self, worth, cost):
        super().__init__(worth, cost)
        self.taxe = self.worth / 1000


class Car(Property):
    """
    Класс машина. Родитель: Property
    Args:
        worth (int): передается стоимость машины
        cost (int): передается количество денег
    Attributes:
        taxe (int): расчет надога на машину
    """
    def __init__(self, worth, cost):
        super().__init__(worth, cost)
        self.taxe = self.worth / 200


class CountryHouse(Property):
    """
    Класс дача. Родитель: Property
    Args:
        worth (int): передается стоимость дачи
        cost (int): передается количество денег
    Attributes:
        taxe (int): расчет надога на дачу
    """
    def __init__(self, worth, cost):
        super().__init__(worth, cost)
        self.taxe = self.worth / 500


property_value = int(input('Стоимость имущества? '))
money = int(input('Сколько денег у пользователя? '))

apart = Apartment(property_value, money)
car = Car(property_value, money)
countryhouse = CountryHouse(property_value, money)
apart.calculation()
