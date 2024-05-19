from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


# Функция для создания клавиатуры с локациями городов
def gen_markup(calldata):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for city in calldata:
        markup.add(InlineKeyboardButton(text=f"{city['name']}, {city['country']}, {city['state']}",
                                        callback_data=f"lat={city['lat']}&lon={city['lon']}"))
    return markup


# Функция для создания клавиатуры с возможностью узнать прогноз погоды на ближайшие 5 суток
def show_weather_forecast():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton(text='Выбрать другой город', callback_data='other_city'),
               InlineKeyboardButton(text='Узнать прогноз на ближайшие сутки', callback_data='forecast'))
    return markup


# Функция для создания клавиатуры с прогнозом максимальной и минимальной температуры
def select_max_min_temperature():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton(text='Максимальная температура', callback_data='maxim_temp'),
               InlineKeyboardButton(text='Минимальная температура', callback_data='minim_temp'))
    return markup
