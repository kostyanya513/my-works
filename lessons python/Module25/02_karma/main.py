import random


class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError'


class KillError(Exception):
    def __str__(self):
        return 'KillError'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError'


class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError'


class Karma:
    """
    Класс кармы буддиста
    Attributes:
        karma (int): карма буддиста
    """
    karma = 500

    def one_day(self):
        """
        Метод одного дня
        :return: количество кармы
        :rtype: int
        """
        while True:
            if random.randint(1, 10) == 1:
                exeption = random.choice([
                    KillError(),
                    DrunkError(),
                    CarCrashError(),
                    GluttonyError(),
                    DepressionError()])
                raise exeption
            else:
                return random.randint(1, 7)

    def life(self):
        """
        Метод достижения просветления буддиста
        :return: выводит на экран информацию о достижении просветления
        """
        while True:
            with open('karma.log', 'a', encoding='utf8') as file:
                try:
                    self.karma -= self.one_day()
                except Exception as ex:
                    file.write('{}\n'.format(ex))
            if self.karma <= 0:
                print('Достиг просветления!')
                break


k = Karma()
k.life()
