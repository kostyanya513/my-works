import requests
import json

from config_data.config import API_KEY
from telebot.types import CallbackQuery
from api.api import API_COORD
from loader import bot


# Этот хэндлер будет обрабатывать нажатую кнопку с локацией и выводить погоду
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call: CallbackQuery) -> None:
    if call.data:
        bot.answer_callback_query(callback_query_id=call.id, text=f'Погода в городе:\n')
        weather_res = requests.get(url=f"{API_COORD}{call.data}&appid={API_KEY}&units=metric", timeout=10)
        data_weather = json.loads(s=weather_res.text)
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Погода в городе: {data_weather['name']}\n"
                              f"Температура воздуха: {data_weather['main']['temp']} C\n"
                              f"Атмосферное давление воздуха: {data_weather['main']['pressure']} ГПа\n"
                              f"Влажность: {data_weather['main']['humidity']} %\n"
                              f"Скорость ветра: {data_weather['wind']['speed']} метр/сек"
                         )
