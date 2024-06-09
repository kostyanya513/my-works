from telebot.types import Message

from database.models import db, User
from loader import bot
from states.state_bot import MyStates
from keyboards.inline.loc_button import gen_markup
from api import api
from utils.dataunix import get_unix_datatime


# Этот хэндлер проверяет полученный файл API,
# формирует клавиатуру с кнопками возможных локаций,
# сохраняет запрос в базу данных
@bot.message_handler(state=[MyStates.start])
def location_request(message: Message) -> None:
    res = api.get_location(q=message.text)
    if res:
        user_id = message.from_user.id
        request_id = 'запрос температуры в городе'
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        data_at = get_unix_datatime(message.date)
        with db:
            User.create(
                    user_id=user_id,
                    request_id=request_id,
                    first_name=first_name,
                    last_name=last_name,
                    data_at=data_at
            )
        bot.set_state(user_id=message.from_user.id, state=MyStates.now_weather, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text=f'Уточните пожалуйста!', reply_markup=gen_markup(res))
    else:
        bot.reply_to(message=message, text='Такого города нет! Попробуйте заново!')
    