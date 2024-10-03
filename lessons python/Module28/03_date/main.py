class Date:
    """
    Класс проверяет дату на корректность и конвертирует строку даты в объект класса
    Args:
        day (int): число месяца
        month (int): месяц года
        year (int): год
    """
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return 'День: {}\tМесяц: {}\tГод: {}'.format(
            self.day, self.month, self.year
        )

    @classmethod
    def from_string(cls, text_data: str) -> 'Date':
        """
        Метод для конвертации строки даты в объект класса Date
        :param text_data: строка даты
        :return: объект класса Date
        """
        int_data = text_data.split('-')
        day, month, year = int(int_data[0]), int(int_data[1]), int(int_data[2])
        data_object = cls(day, month, year)
        if data_object.is_date_valid(text_data):
            return data_object
        else:
            print('Некорректная дата!')

    @classmethod
    def is_date_valid(cls, text_data: str) -> bool:
        """
        Метод для проверки даты на корректность даты
        :param text_data: строка даты
        :return: bool
        """
        int_data = text_data.split('-')
        day, month, year = int(int_data[0]), int(int_data[1]), int(int_data[2])
        if 1 <= month <= 12 or year < 0:
            if (int_data[1] == 2 and 1 <= day <= 28) \
                    or (month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31) \
                    or (month in [4, 6, 9, 11] and 1 <= day <= 30):
                return True
            else:
                return False


date = Date.from_string('90-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
