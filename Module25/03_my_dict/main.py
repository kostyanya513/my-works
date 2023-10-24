class Dict:
    """
    Базовый класс, описывающий словарь
    __slovar: словарь
    """
    __slovar = {1: 'first', 2: 'second', 3: 'therd'}

    def get_slovar(self):
        """
        Геттер для получения словаря
        :return: __slovar
        :rtype: dict
        """
        return self.__slovar

    def get(self, key):
        """
        Геттер для получения значения словаря
        :param key: ключ
        :return: значение или None
        """
        if key in self.__slovar:
            return self.__slovar[key]
        else:
            return None


class MyDict(Dict):
    """
    Класс моего словаря. Родитель: Dict
    __slovar: словарь
    """
    def get(self, key):
        """
        Геттер для получения значения словаря
        :param key: ключ
        :return: значение или 0
        """
        if key in self.get_slovar():
            return self.get_slovar()[key]
        else:
            return 0


mydict = MyDict()
print(mydict.get(4))
