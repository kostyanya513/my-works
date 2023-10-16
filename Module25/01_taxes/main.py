class Property:
    def __init__(self, worth, cost):
        self.worth = worth
        self.cost = cost
        self.taxe = self.worth / 1

    def reshenie(self):
        if self.cost - self.taxe >= 0:
            print('Налог {}'.format(self.taxe))
        elif self.cost - self.taxe < 0:
            print('Налог {}, не хватает {}'.format(
                self.taxe, (self.cost - self.taxe))
            )


class Apartment(Property):
    def __init__(self, worth, cost):
        super().__init__(worth, cost)
        self.taxe = self.worth / 1000


class Car(Property):
    def __init__(self, worth, cost):
        super().__init__(worth, cost)
        self.taxe = self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth, cost):
        super().__init__(worth, cost)
        self.taxe = self.worth / 500


costul = int(input('Стоимость имущества? '))
money = int(input('Сколько денег у пользователя? '))

apart = Apartment(costul, money)
car = Car(costul, money)
countryhouse = CountryHouse(costul, money)
apart.reshenie()
