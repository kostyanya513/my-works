from telebot.types import Message

from loader import bot


# Этот хэндлер будет срабатывать на команду "/start" -
# отправлять приветственное сообщение пользователю,
# прелагать ввести город или показать правила
@bot.message_handler(commands=["start"])
def bot_start(message: Message) -> None:
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!\n"
                          f"Я бот, который показывает погоду.\n"
                          f"В каком городе ты хочешь узнать погоду?\n"
                          f"Могу подсказать правила? /help"
                 )
