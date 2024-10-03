import re
from typing import List


# Функция возвращает координаты
def get_pattern(string: str) -> List:
    pattern_coord = r'[-]?\d{,3}[.]\d{,9}+'
    res = re.findall(pattern_coord, string)
    return res
