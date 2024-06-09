from datetime import datetime
import tzlocal


# Функция преобразует дату и время из формата unix в формат, понятный для пользователя
def get_unix_datatime(date: int) -> str:
    unix_timestamp = float(date)
    local_timezone = tzlocal.get_localzone()
    local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
    return local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)")
