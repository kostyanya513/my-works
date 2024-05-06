from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Функция для создания клавиатуры по заданным параметрам
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton(text='Координаты', callback_data='cb_coord'),
               InlineKeyboardButton(text='Погода', callback_data='cb_weather'),
               InlineKeyboardButton(text='Главные', callback_data='cb_mains'),
               InlineKeyboardButton(text='Ветер', callback_data='cb_wind'),
               InlineKeyboardButton(text='Облака', callback_data='cb_clouds'))
    return markup
