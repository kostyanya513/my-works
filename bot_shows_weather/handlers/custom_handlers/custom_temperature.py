from telebot.types import Message

from database.models import db, User
from loader import bot
from states.state_bot import MyStates
from api import api
from utils.dataunix import get_unix_datatime


# Этот хэндлер запоминает верхнюю точку температурного диапазона и выводит результаты запроса
# и сохраняет запрос в базу данных
@bot.message_handler(state=[MyStates.upper_temperature_point], is_digit=True)
def bot_cancel(message: Message) -> None:
    with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data_location:
        data_location['upper_temp'] = message.text
    with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data_location:
        res = api.get_temp(lat=data_location['lat'], lon=data_location['lon'])
    if res:
        user_id = message.from_user.id
        request_id = 'кастомный запрос'
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        data_at = get_unix_datatime(message.date)
        with db:
            User.create(
                    user_id=user_id,
                    request_id=request_id,
                    first_name=first_name,
                    last_name=last_name,
                    data_at=data_at
            )
        n = 0
        for i in res['list']:
            if int(data_location['lower_temp']) < i['main']['temp'] < int(data_location['upper_temp']) and n < 5:
                bot.send_message(chat_id=message.chat.id,
                                 text=f"Температура {i['main']['temp']} градусов будет {i['dt_txt']}")
                n += 1
            else:
                break
        bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text=f'Для ввода города нажмите /start')
    else:
        bot.reply_to(message=message, text='Такого города нет! Попробуйте заново!')
