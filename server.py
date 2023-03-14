import os

import vk_api
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll

load_dotenv()

vk_session = vk_api.VkApi(token=os.environ.get("VK_TOKEN"))
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
