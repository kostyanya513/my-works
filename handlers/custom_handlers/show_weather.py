from telebot.types import CallbackQuery

from keyboards.inline.loc_button import show_weather_forecast
from loader import bot
from utils import pattern
from states.state_bot import MyStates
from api import api


# Этот хэндлер будет обрабатывать нажатую кнопку с локацией и выводить погоду
@bot.callback_query_handler(func=lambda call: True, state=[MyStates.now_weather])
def show_weather_today(call: CallbackQuery) -> None:
    if call.data:
        coord_city = pattern.get_pattern(call.data)
        with bot.retrieve_data(user_id=call.from_user.id, chat_id=call.message.chat.id) as data_location:
            data_location['lat'] = float(coord_city[0])
            data_location['lon'] = float(coord_city[1])
        bot.send_message(chat_id=call.message.chat.id, text=data_location)
        weather_res = api.get_coord(lat=data_location['lat'], lon=data_location['lon'])
        bot.set_state(user_id=call.from_user.id, state=MyStates.weather_forecast, chat_id=call.message.chat.id)
        bot.send_message(chat_id=call.message.chat.id, text=weather_res)
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Погода в городе: {weather_res['name']}\n"
                              f"Температура воздуха: {weather_res['main']['temp']} C\n"
                              f"Атмосферное давление воздуха: {weather_res['main']['pressure']} ГПа\n"
                              f"Влажность: {weather_res['main']['humidity']} %\n"
                              f"Скорость ветра: {weather_res['wind']['speed']} метр/сек"
                         )
        bot.send_message(chat_id=call.message.chat.id,
                         text=f'Желаете выбрать другой город или хотите посмотреть прогноз погоды на ближайшие сутки?',
                         reply_markup=show_weather_forecast())
