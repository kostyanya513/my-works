from telebot.types import Message
import requests
import json

from api.api import API_GEO
from config_data.config import API_KEY
from loader import bot
from states.state_bot import MyStates
from keyboards.inline.loc_button import gen_markup


# Этот хендлер проверяет полученный файл API и
# формирует клавиатуру с кнопками возможных локаций
@bot.message_handler(state=[MyStates.start, MyStates.now_weather])
def city_weather(message: Message) -> None:
    res = requests.get(f"{API_GEO}{message.text}&limit=5&appid={API_KEY}", timeout=10)
    weather_town = json.loads(s=res.text)
    if weather_town:
        bot.set_state(user_id=message.from_user.id, state=MyStates.now_weather, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text=f'Уточните пожалуйста!', reply_markup=gen_markup(weather_town))
    else:
        bot.reply_to(message=message, text='Такого города нет! Попробуйте заново!')
