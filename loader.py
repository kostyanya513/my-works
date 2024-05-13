from telebot import TeleBot, custom_filters
from telebot.storage import StateMemoryStorage

from config_data import config

# Создаем хранилище для загрузки состояний
storage = StateMemoryStorage()

# Создаем объект бота
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)


# Регистрируем фильтры
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())
