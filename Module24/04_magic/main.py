class Voda:
    def __init__(self, name='Вода'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Vozduh):
            return Shorm()
        elif isinstance(other, Ogon):
            return Par()
        elif isinstance(other, Zemla):
            return Graz()


class Vozduh:
    def __init__(self, name='Воздух'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Ogon):
            return Molnia()
        elif isinstance(other, Zemla):
            return Pil()


class Ogon:
    def __init__(self, name='Огонь'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Zemla):
            return Lava()


class Zemla:
    def __init__(self, name='Земля'):
        self.name = name


class Shorm:
    name = 'Шторм'


class Par:
    name = 'Пар'


class Graz:
    name = 'Грязь'


class Molnia:
    name = 'Молния'


class Pil:
    name = 'Пыль'


class Lava:
    name = 'Лава'


voda = Voda()
vozduh = Vozduh()
ogon = Ogon()
zemla = Zemla()
a = voda + vozduh
b = voda + ogon
c = voda + zemla
d = vozduh + ogon
e = vozduh + zemla
g = ogon + zemla
print(voda.name, '+', vozduh.name, '=', a.name)
print(voda.name, '+', ogon.name, '=', b.name)
print(voda.name, '+', zemla.name, '=', c.name)
print(vozduh.name, '+', ogon.name, '=', d.name)
print(vozduh.name, '+', zemla.name, '=', e.name)
print(ogon.name, '+', zemla.name, '=', g.name)
