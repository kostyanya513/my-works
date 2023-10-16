import random


class CarCrashError(Exception):
    pass


class DrunkError(Exception):
    pass


class KillError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class Karma:
    karma = 500

    @staticmethod
    def errors(num):
        with open('karma.log', 'a', encoding='utf8') as file:
            try:
                if num == 1:
                    file.write('KillError' + '\n')
                    raise KillError
                elif num == 2:
                    file.write('DrunkError' + '\n')
                    raise DrunkError
                elif num == 3:
                    file.write('CarCrashError' + '\n')
                    raise CarCrashError
                elif num == 4:
                    file.write('GluttonyError' + '\n')
                    raise GluttonyError
                elif num == 5:
                    file.write('DepressionError' + '\n')
                    raise DepressionError
                else:
                    return random.randint(1, 7)
            except KillError:
                pass
            except DrunkError:
                pass
            except CarCrashError:
                pass
            except GluttonyError:
                pass
            except DepressionError:
                pass

    def one_day(self):
        while True:
            index = random.randint(1, 10)
            if 1 <= index <= 5:
                self.errors(index)
                return 0
            else:
                return random.randint(1, 7)

    def life(self):
        while True:
            self.karma -= self.one_day()
            if self.karma <= 0:
                print('Достиг просветления!')
                break


k = Karma()
k.life()
