from telebot.types import Message

from loader import bot
from states.state_bot import MyStates
from keyboards.inline.loc_button import gen_markup
from api import api


# Этот хэндлер проверяет полученный файл API и
# формирует клавиатуру с кнопками возможных локаций
@bot.message_handler(state=[MyStates.start])
def location_request(message: Message) -> None:
    res = api.get_location(q=message.text)
    if res:
        bot.set_state(user_id=message.from_user.id, state=MyStates.now_weather, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text=f'Уточните пожалуйста!', reply_markup=gen_markup(res))
    else:
        bot.reply_to(message=message, text='Такого города нет! Попробуйте заново!')
