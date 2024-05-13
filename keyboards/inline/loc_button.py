from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


# Функция для создания клавиатуры по заданным параметрам
def gen_markup(data):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for city in data:
        markup.add(InlineKeyboardButton(text=f"{city['name']}, {city['country']}, {city['state']}",
                                        callback_data=f"lat={city['lat']}&lon={city['lon']}"))
    return markup
