from telebot.types import CallbackQuery
from database.received_weather import user_dict_weather

from loader import bot


# Этот хэндлер будет обрабатывать шаблон погоды "user_dict_weather"
# и в зависимости от нажатой кнопки выдавать параметры
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call: CallbackQuery) -> None:
    if call.data == 'cb_coord':
        bot.answer_callback_query(callback_query_id=call.id, text='/cb_coord')
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Координаты - Долгота: {user_dict_weather['coord']['lon']};"
                              f" Широта: {user_dict_weather['coord']['lat']}")
    elif call.data == 'cb_weather':
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Погода: {user_dict_weather['weather'][0]['main']}\n"
                              f"Погодные условия: {user_dict_weather['weather'][0]['description']}")
    elif call.data == 'cb_mains':
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Температура в Кельвинах: {user_dict_weather['main']['temp']}\n"
                              f"Ощущается как: {user_dict_weather['main']['feels_like']}\n"
                              f"Атмосферное давление: {user_dict_weather['main']['pressure']}\n"
                              f"Влажность: {user_dict_weather['main']['humidity']}\n"
                              f"Минимальная температура: {user_dict_weather['main']['temp_min']}\n"
                              f"Максимальная температура: {user_dict_weather['main']['temp_max']}\n")
    elif call.data == 'cb_wind':
        bot.send_message(chat_id=call.message.chat.id, text=f"Скорость ветра: {user_dict_weather['wind']['speed']}\n"
                                                            f"Направление ветра: {user_dict_weather['wind']['deg']}")
    elif call.data == 'cb_clouds':
        bot.send_message(chat_id=call.message.chat.id, text=f"Облачнось - {user_dict_weather['clouds']['all']}")
