from vk_api.keyboard import VkKeyboard, VkKeyboardColor

keyboard_start = VkKeyboard(one_time=True)
keyboard_start.add_button('Выпечка', color=VkKeyboardColor.PRIMARY)
keyboard_start.add_button('Кондитерская', color=VkKeyboardColor.PRIMARY)
keyboard_start.add_button('Торты', color=VkKeyboardColor.PRIMARY)

keyboard_bakery = VkKeyboard(one_time=True)
keyboard_bakery.add_button("Молочно-сливочная булка", color=VkKeyboardColor.POSITIVE)
keyboard_bakery.add_line()
keyboard_bakery.add_button("Сытный многозерновой хлеб", color=VkKeyboardColor.POSITIVE)
keyboard_bakery.add_line()
keyboard_bakery.add_button("Хлеб с томатами и луковыми чипсами", color=VkKeyboardColor.POSITIVE)
keyboard_bakery.add_line()
keyboard_bakery.add_button("Назад", color=VkKeyboardColor.SECONDARY)

keyboard_confectionery = VkKeyboard(one_time=True)
keyboard_confectionery.add_button("Пирожное Жоло", color=VkKeyboardColor.POSITIVE)
keyboard_confectionery.add_line()
keyboard_confectionery.add_button("Шоколадный кекс", color=VkKeyboardColor.POSITIVE)
keyboard_confectionery.add_line()
keyboard_confectionery.add_button("Назад", color=VkKeyboardColor.SECONDARY)

keyboard_cakes = VkKeyboard(one_time=True)
keyboard_cakes.add_button("Торт лесная сказка", color=VkKeyboardColor.POSITIVE)
keyboard_cakes.add_line()
keyboard_cakes.add_button("Фисташковый торт", color=VkKeyboardColor.POSITIVE)
keyboard_cakes.add_line()
keyboard_cakes.add_button("Назад", color=VkKeyboardColor.SECONDARY)