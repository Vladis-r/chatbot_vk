import vk_api
from vk_api.utils import get_random_id

from server import vk


def get_attachment_photo(photo: str):
    """
    Загружает фото на сервер вк.
    :param photo: путь к фото.
    :return: Возвращает ссылку на фото.
    """
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(photo)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'

    return attachment


def send_message(message: str, user_id: int, keyboard=None, attachment=None):
    """
    Отправка сообщений в чат сообщества.
    :param message: текст сообщения
    :param user_id: ид пользователя
    :param keyboard: клавиатура, если есть.
    :param attachment: фото, если есть.
    """
    if keyboard:
        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            keyboard=keyboard.get_keyboard(),
            attachment=attachment,
            message=message
        )
    else:
        vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            attachment=attachment,
            message=message
        )
