from telebot.types import Message

from loader import bot


# Этот хэндлер срабатывает на команду "/cancel" - сбрасывает текущее состояние бота
@bot.message_handler(state="*", commands=["cancel"])
def bot_cancel(message: Message) -> None:
    bot.send_message(chat_id=message.chat.id, text=f"Запустите бота заново командой /start, если желаете узнать погоду")
    bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)
