from telebot.types import Message
import requests
import json
from api.api import API_TOWN
from loader import bot
from config_data.config import API_KEY
from keyboards.inline.loc_button import gen_markup
from database.received_weather import user_dict_weather


# Этот хэндлер будет реагировать на любые сообщения, кроме "/start" и "/help" -
# если город введен корректно, то записывает данные о погоде в словарь, создает клавиатуру с командами;
# если город введен не корректно, то просит ввести корректное название города
@bot.message_handler(content_types=['text'])
def bot_weather_town(message: Message) -> None:
    res = requests.get(f"{API_TOWN}{message.text}&units=metric&lang=ru&appid={API_KEY}")
    weather_town = json.loads(res.text)
    if res.status_code == 200:
        bot.send_message(chat_id=message.chat.id, text='Что вы хотите знать?', reply_markup=gen_markup())
        user_dict_weather.update(weather_town)
    else:
        bot.send_message(chat_id=message.chat.id, text='Попробуйте ввести город еще раз!')
