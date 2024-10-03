class MyDict(dict):
    """
    Класс моего словаря. Родитель: dict
    """
    def get(self, key, default=0):
        """
        Переопределение метода get для словаря
        :param default: 0
        :param key: ключ
        :return: значение или 0
        """
        return super().get(key, default)


mydict = MyDict()
mydict['a'] = 1
print(mydict.get('b'))
