from telebot.types import CallbackQuery

from loader import bot
from api import api
from states.state_bot import MyStates
from database.models import User, db
from utils.dataunix import get_unix_datatime


# Этот хэндлер срабатывает, при нажатии на кнопку "Максимальная температура",
# выводит на экран прогноз по максимальной температуре,
# сохраняет запрос в базу данных
@bot.callback_query_handler(func=lambda call: call.data == 'maxim_temp', state=[MyStates.select_temp])
def get_max_temp(call: CallbackQuery) -> None:
    with bot.retrieve_data(user_id=call.from_user.id, chat_id=call.message.chat.id) as data_location:
        res = api.get_temp(lat=data_location['lat'], lon=data_location['lon'])
    if res:
        user_id = call.from_user.id
        request_id = 'запрос максимальной температуры'
        first_name = call.from_user.first_name
        last_name = call.from_user.last_name
        data_at = get_unix_datatime(call.message.date)
        with db:
            User.create(
                user_id=user_id,
                request_id=request_id,
                first_name=first_name,
                last_name=last_name,
                data_at=data_at
            )
        list_max_temp = [index['main']['temp_max'] for index in res['list']]
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"В ближайшие 5 суток максимальная температура {max(list_max_temp)} градусов Цельсия")
        bot.delete_state(user_id=call.from_user.id, chat_id=call.message.chat.id)
        bot.send_message(chat_id=call.message.chat.id, text=f'Для ввода города нажмите /start')
    else:
        bot.reply_to(message=call.message, text='Такого города нет! Попробуйте заново!')
