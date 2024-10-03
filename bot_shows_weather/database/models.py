import datetime
from peewee import (
    CharField,
    IntegerField,
    Model,
    SqliteDatabase, DateTimeField
)

from config_data.config import DB_PATH

db = SqliteDatabase(DB_PATH) # Создаем объект базы данных


# Создаем класс, чтобы наследовать от него все таблицы базы данных
class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    # Описываем таблицу базы данных
    user_id = IntegerField()
    first_name = CharField()
    last_name = CharField(null=True)
    request_id = CharField()
    data_at = DateTimeField(default=datetime.datetime.now())


User.create_table()  # Создаем таблицу
