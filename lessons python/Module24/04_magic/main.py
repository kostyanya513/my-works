class Water:
    def __init__(self, name='Вода'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mire()


class Air:
    def __init__(self, name='Воздух'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()


class Fire:
    def __init__(self, name='Огонь'):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()


class Earth:
    def __init__(self, name='Земля'):
        self.name = name


class Storm:
    name = 'Шторм'


class Steam:
    name = 'Пар'


class Mire:
    name = 'Грязь'


class Lightning:
    name = 'Молния'


class Dust:
    name = 'Пыль'


class Lava:
    name = 'Лава'


water = Water()
air = Air()
fire = Fire()
earth = Earth()
a = water + air
b = water + fire
c = water + earth
d = air + fire
e = air + earth
g = fire + earth
print(water.name, '+', air.name, '=', a.name)
print(water.name, '+', fire.name, '=', b.name)
print(water.name, '+', earth.name, '=', c.name)
print(air.name, '+', fire.name, '=', d.name)
print(air.name, '+', earth.name, '=', e.name)
print(fire.name, '+', earth.name, '=', g.name)
