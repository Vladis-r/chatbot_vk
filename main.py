from vk_api.longpoll import VkEventType

from db.db_query import QueryItem, QueryCategory
from keyboards import keyboard_start, keyboard_bakery, keyboard_confectionery, keyboard_cakes
from server import longpoll
from utils import get_attachment_photo, send_message


class BotRunner:
    """
    Основной класс взаимодействия с ботом.
    Имеет 5 видов состояний (bot_condition)
    """

    def __init__(self, bot_condition: int = 1):
        self.bot_condition = bot_condition
        self.keyboards = {1: keyboard_start,
                          2: keyboard_start,
                          3: keyboard_bakery,
                          4: keyboard_confectionery,
                          5: keyboard_cakes}

    def run_bot(self):
        while self.bot_condition == 1:
            self.bot_condition += 1
            yield send_message('Добро пожаловать в нашу пекарню! Выберите раздел:', event.user_id,
                               keyboard=keyboard_start)

        while self.bot_condition == 2:
            query_category = QueryCategory(event.message, self.bot_condition)
            if bool(query_category):
                self.bot_condition = query_category.condition
                yield send_message('Выбирайте:', event.user_id, keyboard=self.keyboards[self.bot_condition])
            else:
                yield send_message("Нет такой категории", event.user_id, keyboard=self.keyboards[self.bot_condition])

        while self.bot_condition in [3, 4, 5]:
            query_item = QueryItem(event.message, self.bot_condition)
            if bool(query_item):
                yield send_message(query_item.description, event.user_id, keyboard=self.keyboards[self.bot_condition],
                                   attachment=get_attachment_photo(query_item.link))

            elif event.message == "Назад":
                self.bot_condition = 1
                yield next(self.run_bot())

            else:
                yield send_message("Нет такого продукта", event.user_id, keyboard=self.keyboards[self.bot_condition])


bot_runner = BotRunner()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        next(bot_runner.run_bot())
