import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
API_GEO = 'http://api.openweathermap.org/geo/1.0/direct'  # API геокодирования
API_COORD = 'https://api.openweathermap.org/data/2.5/weather'  # API погоды по координатам
API_TEMP = 'https://api.openweathermap.org/data/2.5/forecast'  # API прогноза погоды на 5 суток
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("cancel", "Начать заново")
)
