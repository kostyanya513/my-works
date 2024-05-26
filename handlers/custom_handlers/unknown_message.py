from telebot.types import Message

from loader import bot


# Этот хэндлер срабатывает на любую неизвестную команду
@bot.message_handler(state="*")
def bot_cancel(message: Message) -> None:
    bot.send_message(chat_id=message.chat.id, text=f"Вы ввели неизвестную команду, повторите ввод")
