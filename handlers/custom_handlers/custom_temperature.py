from telebot.types import Message

from loader import bot
from states.state_bot import MyStates
from api import api


# Этот хэндлер запоминает верхнюю точку температурного диапазона и выводит результаты запроса
@bot.message_handler(state=[MyStates.upper_temperature_point], is_digit=True)
def bot_cancel(message: Message) -> None:
    with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data_location:
        data_location['upper_temp'] = message.text
    with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data_location:
        res = api.get_temp(lat=data_location['lat'], lon=data_location['lon'])
    if res:
        for i in res['list']:
            if int(data_location['lower_temp']) < i['main']['temp'] < int(data_location['upper_temp']):
                bot.send_message(chat_id=message.chat.id, text=f"Температура {i['main']['temp']} градусов будет {i['dt_txt']}")
        bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text=f'Для ввода города нажмите /start')
    else:
        bot.reply_to(message=message, text='Такого города нет! Попробуйте заново!')
