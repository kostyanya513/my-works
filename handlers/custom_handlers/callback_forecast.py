from telebot.types import CallbackQuery

from keyboards.inline.loc_button import select_max_min_temperature
from loader import bot
from states.state_bot import MyStates


# Этот хэндлер срабатывает, если пользователь хочет узнать прогноз погоды на ближайшие 5 суток
@bot.callback_query_handler(func=lambda call: call.data == 'forecast', state=[MyStates.weather_forecast])
def get_forecast(call: CallbackQuery) -> None:
    bot.set_state(user_id=call.from_user.id, state=MyStates.select_temp, chat_id=call.message.chat.id)
    bot.send_message(chat_id=call.message.chat.id, text='Какую температуру желаете узнать?',
                     reply_markup=select_max_min_temperature())
    
