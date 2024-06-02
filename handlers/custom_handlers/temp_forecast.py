from telebot.types import CallbackQuery

from loader import bot
from states.state_bot import MyStates


# Этот хэндлер срабатывает, при нажатии на кнопку "Узнать температурный прогноз"
# и просит ввести диапазон температур
@bot.callback_query_handler(func=lambda call: call.data == 'temp_data', state=[MyStates.weather_forecast])
def get_lower_temp(call: CallbackQuery) -> None:
    bot.set_state(user_id=call.from_user.id, state=MyStates.lower_temperature_point, chat_id=call.message.chat.id)
    bot.send_message(chat_id=call.message.chat.id, text=f'Теперь нужно ввести диапазон температур\n'
                                                        f'Введите нижнюю границу запроса температуры')
