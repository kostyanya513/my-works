import requests
import json

from config_data.config import API_KEY
from api.api import API_TEMP
from telebot.types import CallbackQuery
from loader import bot
from database.database import data


# Этот хэндлер срабатывает, при нажатии на кнопку "Минимальная температура"
# и выводит на экран прогноз по минимальной температуре
@bot.callback_query_handler(func=lambda call: call.data == 'minim_temp')
def callback_query(call: CallbackQuery) -> None:
    res = requests.get(f"{API_TEMP}{data[-1]}&appid={API_KEY}&units=metric", timeout=10)
    forecast_weather_town = json.loads(s=res.text)
    if forecast_weather_town:
        list_max_temp = [index['main']['temp_min'] for index in forecast_weather_town['list']]
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"В ближайшие 5 суток минимальная температура {min(list_max_temp)} градусов Цельсия")
    else:
        bot.reply_to(message=call.message, text='Такого города нет! Попробуйте заново!')
