from vk_api.longpoll import VkEventType

from keyboards import keyboard_start, keyboard_bakery, keyboard_confectionery, keyboard_cakes
from server import longpoll
from utils import get_attachment_photo, send_message


class BotRunner:
    def __init__(self, bot_condition: int = 1):
        self.bot_condition = bot_condition

    def run_bot(self):
        while self.bot_condition == 1:
            self.bot_condition += 1
            yield send_message('Добро пожаловать в нашу пекарню! Выберите раздел:', event.user_id,
                               keyboard=keyboard_start)

        while self.bot_condition == 2:
            if event.message == "Выпечка":
                self.bot_condition += 1
                yield send_message('Выбирайте:', event.user_id, keyboard=keyboard_bakery)
            elif event.message == "Кондитерская":
                self.bot_condition += 2
                yield send_message('Выбирайте:', event.user_id, keyboard=keyboard_confectionery)
            elif event.message == "Торты":
                self.bot_condition += 3
                yield send_message('Выбирайте:', event.user_id, keyboard=keyboard_cakes)

        while self.bot_condition == 3:
            if event.message == "Молочно-сливочная булка":
                message = 'Хлеб высокий, пышный, с отчетливым сливочно-молочным ароматом и вкусом.'
                yield send_message(message, event.user_id, keyboard=keyboard_bakery,
                                   attachment=get_attachment_photo('data/молочно-сливочная булка.png'))

            elif event.message == "Сытный многозерновой хлеб":
                message = 'Этот хлеб печется на полезной цельнозерновой муке с добавлением овсяных хлопьев, дополнен семенами и орехами, очень вкусный и сытный!'
                yield send_message(message, event.user_id, keyboard=keyboard_bakery,
                                   attachment=get_attachment_photo('data/cытный многозерновой хлеб.jpg'))

            elif event.message == "Хлеб с томатами и луковыми чипсами":
                message = 'Совершенно чудесный, самодостаточный хлеб с вялеными томатами и луковыми чипсами на закваске.'
                yield send_message(message, event.user_id, keyboard=keyboard_bakery, attachment=get_attachment_photo(
                    'data/Хлеб с томатами и луковыми чипсами.jpg'))

            elif event.message == "Назад":
                self.bot_condition = 1
                yield next(self.run_bot())

            else:
                yield send_message("Нет такого продукта", event.user_id, keyboard=keyboard_bakery)

        while self.bot_condition == 4:
            if event.message == "Пирожное Жоло":
                message = "Очень нежное и ароматное. Крем на вкус напоминает клубничный йогурт."
                yield send_message(message, event.user_id, attachment=get_attachment_photo("data/Пирожное Жоло.jpg"),
                                   keyboard=keyboard_confectionery)

            elif event.message == "Шоколадный кекс":
                message = 'Легкий и вкусный шоколадный кекс с лесными ягодами.'
                yield send_message(message, event.user_id, attachment=get_attachment_photo('data/шоколадный кекс.jpg'),
                                   keyboard=keyboard_confectionery)

            elif event.message == "Назад":
                self.bot_condition = 1
                yield next(self.run_bot())

            else:
                yield send_message("Нет такого продукта", event.user_id, keyboard=keyboard_confectionery)

        while self.bot_condition == 5:
            if event.message == "Фисташковый торт":
                message = """Шикарный фисташковый торт. Коржи приятного зеленого цвета идеально гармонируют 
                с белоснежным крем-чизом и нежно салатовым кремом с фисташковой пастой."""
                yield send_message(message, event.user_id, attachment=get_attachment_photo("data/Фисташковый торт.png"),
                                   keyboard=keyboard_cakes)

            elif event.message == "Торт лесная сказка":
                message = 'Вкуснейший торт, украшенный ягодами голубики и ежевики.'
                yield send_message(message, event.user_id,
                                   attachment=get_attachment_photo('data/Торт лесная сказка.jpg'),
                                   keyboard=keyboard_cakes)

            elif event.message == "Назад":
                self.bot_condition = 1
                yield next(self.run_bot())

            else:
                yield send_message("Нет такого продукта", event.user_id, keyboard=keyboard_cakes)


bot_runner = BotRunner()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        next(bot_runner.run_bot())
