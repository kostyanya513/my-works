from telebot.handler_backends import State, StatesGroup


# Создаем класс, наслелуемый от StatesGroup, для группы состояний
class MyStates(StatesGroup):
    start = State()  # состояние ввода города
