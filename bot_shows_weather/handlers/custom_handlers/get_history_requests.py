from telebot.types import Message

from database.models import User
from loader import bot


# Этот хэндлер срабатывает на команду /history и предоставляет пользователю историю его запросов
@bot.message_handler(commands=["history"])
def get_history_requests(message: Message) -> None:
    for user in User.select():
        bot.send_message(chat_id=message.chat.id,
                         text=f'Запрос {user.id}: дата - {user.data_at}; пользователь - {user.first_name}; {user.request_id}')
