from telebot.types import Message

from loader import bot
from states.state_bot import MyStates


# Этот хэндлер запоминает нижнюю точку температурного диапазона и просит ввести верхнюю точку диапазона
@bot.message_handler(state=[MyStates.lower_temperature_point], is_digit=True)
def get_lower_temp(message: Message) -> None:
    with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data_location:
        data_location['lower_temp'] = message.text
    bot.set_state(user_id=message.from_user.id, state=MyStates.upper_temperature_point, chat_id=message.chat.id)
    bot.send_message(chat_id=message.chat.id, text=f"Введите верхнюю границу запроса температуры")
