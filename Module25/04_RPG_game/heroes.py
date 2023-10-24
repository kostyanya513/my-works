import random


class Hero:
    """
    Базовый класс, опысывающий героя
    Args:
        name (str): имя героя
    Attributes:
        max_hp (int): максимальное здоровье героя
        start_power (int): сила героя
    """

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        """
        Геттер для получения здоровья героя
        :return: __hp
        :rtype: int
        """
        return self.__hp

    def set_hp(self, new_value):
        """
        Сеттер для установления количество здоровья
        :param new_value: здоровье
        :return: new_value
        """
        self.__hp = max(new_value, 0)

    def get_power(self):
        """
        Геттер для получения силы героя
        :return: __power
        :rtype: int
        """
        return self.__power

    def set_power(self, new_power):
        """
        Сеттер для установления количество силы
        :param new_power: сила
        :return: new_value
        """
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    def attack(self, target):
        """
        Метод атаки героя
        :raise: "Вы забыли переопределить метод Attack!"
        """
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        """
        Метод получения урона и вывода информации о здоровье
        """
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ",
              round(self.get_hp()))
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        """
        Метод увеличения силы героя на 0,1
        """
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        """
        Магический метод вывода информации о своем состоянии
        :raise: Вы забыли переопределить метод __str__!
        """
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    """
    Класс Целитель. Родитель: Hero
    Args:
        name (str): имя героя
    Attributes:
        max_hp (int): максимальное здоровье героя
        start_power (int): сила героя
        magic_power (int): магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3
    """

    def __init__(self, name):
        super().__init__(name)
        self.magic_power = self.get_power() * 3

    def attack(self, target):
        """
        Метод атаки - может атаковать врага, но атакует только в половину силы
        """
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        """
        Метод получения урона - т.к. защита целителя слаба - он получает на 20% больше урона
        """
        self.set_hp(self.get_hp() - 1.2 * damage)

    def healing(self):
        """
        Метод исцеления - увеличивает здоровье цели на величину равную своей магической силе
        """
        self.set_hp(self.get_hp() + self.magic_power)

    def make_a_move(self, friends, enemies):
        """
        Метод увеличения силы героя на 0,1
        Args:
            friends (list): союзники
            enemies (list): враги
        Исцеляет союзника, если у него здоровье меньше 60.
        В противном случае атакует ближнего врага.
        """
        self.set_power(self.get_power() + 0.1)
        print(self.name, end=' ')
        chosen_target = friends[0]
        min_health = chosen_target.get_hp()
        if min_health < 60:
            print('Исцеляю', chosen_target.name)
            self.healing()
        else:
            if not enemies:
                return
            print("Атакую ближнего -", enemies[0].name)
            self.attack(enemies[0])
        print('\n')

    def __str__(self):
        """
        Магический метод вывода информации о своем состоянии
        :raise: Вы забыли переопределить метод __str__!
        """
        return '{}: здоровье {}'.format(self.name, self.get_hp())


class Tank(Hero):
    """
    Класс Танк. Родитель: Hero
    Args:
        name (str): имя героя
    Attributes:
        max_hp (int): максимальное здоровье героя
        defense (int): показатель защиты
        shield (bool): сотояние щита
    """

    def __init__(self, name):
        super().__init__(name)
        self.defense = 1
        self.shield = True

    def attack(self, target):
        """
        Метод атаки - может атаковать врага, но с двойной силой
        """
        target.take_damage(self.get_power() * 2)

    def take_damage(self, damage):
        """
        Метод получения урона - весь входящий урон делится на показатель защиты и потом отнимается от здоровья
        """
        self.set_hp(self.get_hp() - (damage / self.defense) / 2)

    def raise_shield(self):
        """
        Метод поднятия щита - если щит не поднят - поднимает щит.
        Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
        """
        if not self.shield:
            self.defense = self.defense * 2
            self.set_power(self.get_power() * 2)

    def lower_shields(self):
        """
        Метод опускания щита - если щит поднят - опускает щит.
        Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
        """
        if self.shield:
            self.defense = self.defense / 2
            self.set_power(self.get_power() / 2)

    def make_a_move(self, friends, enemies):
        """
        Метод увеличения силы героя на 0,1
        Args:
            friends (list): союзники
            enemies (list): враги
        Атакует врага, у которого здоровье больше 60, если такого нет, то поднимает щит если свое здоровье меньше 70.
        Если поднят щит, то опускает его
        """
        self.set_power(self.get_power() + 0.1)
        print(self.name, end=' ')
        if not enemies:
            return
        for enemie in enemies:
            if enemie.get_hp() > 60:
                print('Атакую - ', enemie.name)
                self.attack(enemie)
            else:
                if self.get_hp() < 70:
                    print('{} Поднимает щит!'.format(self.name))
                    self.raise_shield()
                else:
                    print('{} Опускает щит!'.format(self.name))
                    self.lower_shields()
        print('\n')

    def __str__(self):
        """
        Магический метод вывода информации о своем состоянии
        :raise: Вы забыли переопределить метод __str__!
        """
        return '{}: здоровье {}'.format(self.name, self.get_hp())


class Attacker(Hero):
    """
    Класс Убийца. Родитель: Hero
    Args:
        name (str): имя героя
    Attributes:
        max_hp (int): максимальное здоровье героя
        power_multiply (int): коэффициент усиления урона
    """

    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 1

    def attack(self, target):
        """
        Метод атаки - наносит урон равный показателю силы умноженному на коэффициент усиления урона
        после нанесения урона - вызывается метод ослабления power_down.
        """
        target.take_damage(self.get_power() * self.power_multiply)
        self.power_down()

    def take_damage(self, damage):
        """
        Метод получения урона -получает урон равный входящему урона умноженному на половину коэффициента усиления урона
        """
        self.set_hp(self.get_hp() - damage * (self.power_multiply / 2))

    def power_up(self):
        """
        Метод усиления урона- увеличивает коэффициента усиления урона в 2 раза
        """
        self.power_multiply *= 2

    def power_down(self):
        """
        Метод уменьшения урона- уменьшает коэффициента усиления урона в 2 раза
        """
        self.power_multiply /= 2

    def make_a_move(self, friends, enemies):
        """
        Метод увеличения силы героя на 0,1
        Args:
            friends (list): союзники
            enemies (list): враги
        Атакует врага, у которого здоровье больше 60,
        если такого нет, то при коэффициенте усиления меньше 1 увеличивает коэффициент,
        если коэффициент усиления больше 1 - уменьшает коэффициент
        """
        self.set_power(self.get_power() + 0.1)
        print(self.name, end=' ')
        if not enemies:
            return
        for enemie in enemies:
            if enemie.get_hp() > 60:
                print('Атакую - ', enemie.name)
                self.attack(enemie)
            else:
                if self.power_multiply <= 1:
                    self.power_up()
                else:
                    self.power_down()
        print('\n')

    def __str__(self):
        """
        Метод опускания щита - если щит поднят - опускает щит.
        Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
        """
        return '{}: здоровье {}'.format(self.name, self.get_hp())
