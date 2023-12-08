class Date:
    """
    Класс проверяет дату на корректность
    Args:
        text_data (str): дата
    """
    def __init__(self, text_data: str) -> None:
        self.is_date_valid(text_data)

    @classmethod
    def from_string(cls, text_data: str) -> str:
        """
        Метод для конвертации даты
        :param text_data: дата
        :return: дата
        """
        return 'День: {}\tМесяц: {}\tГод: {}'.format(
            text_data.split('-')[0],
            text_data.split('-')[1],
            text_data.split('-')[2]
        )

    @classmethod
    def is_date_valid(cls, text_data: str) -> bool:
        """
        Метод для проверки даты на корректность
        :param text_data: дата
        :return: bool
        """
        int_data = [int(item) for item in text_data.split('-')]
        if 1 <= int_data[1] <= 12 or int_data[2] < 0:
            if (int_data[1] == 2 and 1 <= int_data[0] <= 28) \
                    or (int_data[1] in [1, 3, 5, 7, 8, 10, 12] and 1 <= int_data[0] <= 31) \
                    or (int_data[1] in [4, 6, 9, 11] and 1 <= int_data[0] <= 30):
                return True
            else:
                return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
