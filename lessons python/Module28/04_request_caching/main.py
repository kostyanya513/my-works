class LRUCache:
    """
    Класс, который хранит ограниченное количество объектов и, при превышении лимита,
    удаляет самые давние (самые старые) использованные элементы.
    Args:
        capacity (int): лимит
    Attributes:
        element (list): список объектов
        dict (tuple): словарь объектов
    """
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.element = []
        self.dict = {}

    @property
    def cache(self) -> list:
        """
        Геттер для получения списка объектов
        :return: список объектов
        :rtype: list
        """
        return self.element

    @cache.setter
    def cache(self, key: tuple) -> None:
        """
        Сеттер для создания словаря объектов
        :param key: кортеж объекта
        :rtype: tuple
        :return: словарь объектов
        """
        self.element.append(key)
        if len(self.element) > self.capacity:
            self.element.pop(0)
        self.dict = {key: value for key, value in self.element}

    def print_cache(self) -> None:
        """
        Метод для вывода на экран текущего кеш
        """
        print('\nLRU Cache:')
        for key, value in self.dict.items():
            print('{}\t:\t{}'.format(key, value))

    def get(self, key: str) -> str:
        """
        Метод для вывода на экран значения по ключу и установления элемента по количеству запросов
        :param key: ключ кэша
        :return: значение кэша
        """
        for elem in self.element:
            if key in elem:
                cache_element = self.element.pop(self.element.index(elem))
                self.element.append(cache_element)
        return '\n' + self.dict[key]

# Создаем экземпляр класса LRU Cache с capacity = 3


cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
