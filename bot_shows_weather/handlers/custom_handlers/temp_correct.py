from telebot.types import Message

from loader import bot
from states.state_bot import MyStates


# Этот хэндлер срабатывает, если пользователь вместо температуры ввел не число
@bot.message_handler(state=[MyStates.lower_temperature_point, MyStates.upper_temperature_point], is_digit=False)
def temp_correct(message: Message) -> None:
    bot.send_message(chat_id=message.chat.id, text=f"Температура должна быть числом. Попробуйте еще раз")
