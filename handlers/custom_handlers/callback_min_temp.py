from telebot.types import CallbackQuery

from api import api
from loader import bot
from states.state_bot import MyStates


# Этот хэндлер срабатывает, при нажатии на кнопку "Минимальная температура"
# и выводит на экран прогноз по минимальной температуре
@bot.callback_query_handler(func=lambda call: call.data == 'minim_temp', state=[MyStates.select_temp])
def get_min_temp(call: CallbackQuery) -> None:
    with bot.retrieve_data(user_id=call.from_user.id, chat_id=call.message.chat.id) as data_location:
        res = api.get_temp(lat=data_location['lat'], lon=data_location['lon'])
    if res:
        list_max_temp = [index['main']['temp_min'] for index in res['list']]
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"В ближайшие 5 суток минимальная температура {min(list_max_temp)} градусов Цельсия")
        bot.delete_state(user_id=call.from_user.id, chat_id=call.message.chat.id)
        bot.send_message(chat_id=call.message.chat.id, text=f'Для ввода города нажмите /start')
    else:
        bot.reply_to(message=call.message, text='Такого города нет! Попробуйте заново!')
