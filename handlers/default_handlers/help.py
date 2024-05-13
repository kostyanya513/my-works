from telebot.types import Message

from loader import bot


# Этот хэндлер будет реагировать на команду "/help" -
# показывать правила и предлагать ввести город
@bot.message_handler(commands=["help"])
def bot_help(message: Message) -> None:
    bot.send_message(chat_id=message.chat.id, text=f'Нужно ввести город, а затем выбрать\n'
                                                   f'подходящую локацию из списка.\n')
