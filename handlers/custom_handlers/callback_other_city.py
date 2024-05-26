from telebot.types import CallbackQuery
from loader import bot
from states.state_bot import MyStates


# Этот хэндлер срабатывает если пользователь желает узнать погоду в другом городе
# и просит пользователя ввести город
@bot.callback_query_handler(func=lambda call: call.data == 'other_city')
def callback_query(call: CallbackQuery) -> None:
    bot.set_state(user_id=call.from_user.id, state=MyStates.start, chat_id=call.message.chat.id)
    bot.answer_callback_query(callback_query_id=call.id, text=f'Продолжаем показ погоды!\n')
    bot.send_message(chat_id=call.message.chat.id, text='Введите город')
