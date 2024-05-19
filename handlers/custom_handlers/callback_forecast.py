from telebot.types import CallbackQuery
from keyboards.inline.loc_button import select_max_min_temperature
from loader import bot
from database.database import data


# Этот хэндлер срабатывает, если пользователь хочет узнать прогноз погоды на ближайшие 5 суток
@bot.callback_query_handler(func=lambda call: call.data == 'forecast')
def callback_query(call: CallbackQuery) -> None:
    bot.send_message(chat_id=call.message.chat.id, text='Какую температуру желаете узнать?',
                     reply_markup=select_max_min_temperature())
    print(data)
