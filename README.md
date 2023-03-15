# CHATBOT на платформе VK
## Возможности:
- кнопки в сообщениях сообществу:
  - кнопки категорий;
  - кнопки товаров, кнопка назад;
  - вывод фото и информации о товаре, кнопки с выбором других товаров из той же категории;
- информация хранится в БД (sqlite3);


# Для запуска:
- Установить виртуальное окружение (и активировать его):

        python -m venv venv
        venv\Scripts\activate.bat - активация для Windows
- Установить зависимости:
 
        pip install -r requirements.txt

- Создать и заполнить БД (sqlite3):

		python db/create_db.py 
- Запустить бота:

        python main.py

# При запуске с помощью docker:
- создать контейнер:

        docker build -t <container_name>
- запустить контейнер (необходимо передать аргумент <vk_token>):

        docker run --build-arg token=<vk_token> -t <container_name> .
