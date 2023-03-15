import sqlite3

# Для заполнения бд
data = [
    ("Молочно-сливочная булка", "Хлеб высокий, пышный, с отчетливым сливочно-молочным ароматом и вкусом.", 1, "data/молочно-сливочная булка.png"),
    ("Сытный многозерновой хлеб", "Этот хлеб печется на полезной цельнозерновой муке с добавлением овсяных хлопьев, дополнен семенами и орехами, очень вкусный и сытный!", 1, "data/cытный многозерновой хлеб.jpg"),
    ("Хлеб с томатами и луковыми чипсами", "Совершенно чудесный, самодостаточный хлеб с вялеными томатами и луковыми чипсами на закваске.", 1, "data/Хлеб с томатами и луковыми чипсами.jpg"),
    ("Пирожное Жоло", "Очень нежное и ароматное. Крем на вкус напоминает клубничный йогурт.", 2, "data/Пирожное Жоло.jpg"),
    ("Шоколадный кекс", "Легкий и вкусный шоколадный кекс с лесными ягодами.", 2, "data/шоколадный кекс.jpg"),
    ("Фисташковый торт", "Шикарный фисташковый торт. Коржи приятного зеленого цвета идеально гармонируют с белоснежным крем-чизом и нежно салатовым кремом с фисташковой пастой.", 3, "data/Фисташковый торт.png"),
    ("Торт лесная сказка", "Вкуснейший торт, украшенный ягодами голубики и ежевики.", 3, "data/Торт лесная сказка.jpg")
]


def create_tables():
    """
    Создание базы данных sqlite3.
    2 таблицы.
    categories: id, category_name.
    items: id, item_name, description, category_id, link
    """
    with sqlite3.connect("db/vk_chat_bot.db") as connection:
        cur = connection.cursor()

        sqlite_query = """
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                category_name VARCHAR(255)
            )
        """
        cur.execute(sqlite_query)

        sqlite_query = """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                item_name VARCHAR(255),
                description TEXT, 
                category_id INT,
                link VARCHAR(255),
                FOREIGN KEY (Category_id) REFERENCES categories (Id)
            )
        """
        cur.execute(sqlite_query)
        connection.commit()


def add_data():
    """
    Заполнение базы данных
    """
    with sqlite3.connect("db/vk_chat_bot.db") as connection:
        cur = connection.cursor()
        sqlite_query = """
        INSERT INTO categories (category_name)
        VALUES ('Выпечка'), ('Кондитерская'), ('Торты');"""
        cur.execute(sqlite_query)

        sqlite_query = """
        INSERT INTO items (item_name, description, category_id, link)
        VALUES (?, ?, ?, ?);"""
        cur.executemany(sqlite_query, data)
        connection.commit()


create_tables()
add_data()
