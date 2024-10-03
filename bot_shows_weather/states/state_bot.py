from telebot.handler_backends import State, StatesGroup


# Создаем класс, наследуемый от StatesGroup, для группы состояний
class MyStates(StatesGroup):
    start = State()  # состояние ввода города
    now_weather = State()  # Состояние текущей погоды
    weather_forecast = State()  # Состояние выбора температуры или другого города
    select_temp = State()  # Состояние выбора прогноза температуры
    lower_temperature_point = State()  # Состояние ожидания ввода нижней точки температуры
    upper_temperature_point = State()  # Состояние ожидания ввода верхней точки температуры
