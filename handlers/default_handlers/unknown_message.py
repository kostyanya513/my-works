from telebot.types import Message

from loader import bot


# Этот хэндлер срабатывает на любую неизвестную команду
@bot.message_handler(state="*", content_types=["text"])
def bot_cancel(message: Message) -> None:
    f = bot.get_state(user_id=message.from_user.id, chat_id=message.chat.id)
    bot.send_message(chat_id=message.chat.id, text=f'{f}unknown_message')
    bot.send_message(chat_id=message.chat.id, text=f"Вы ввели неизвестную команду, повторите ввод")
