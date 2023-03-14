import sqlite3


def create_tables():
    with sqlite3.connect("vk_chat_bot.db") as connection:
        cur = connection.cursor()

        sqlite_query = """
            CREATE TABLE IF NOT EXISTS categories (
                Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                Category_name VARCHAR(255)
            )
        """

        cur.execute(sqlite_query)

        sqlite_query = """
            CREATE TABLE IF NOT EXISTS items (
                Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                Item_name VARCHAR(255),
                Description TEXT, 
                Category_id INT,
                FOREIGN KEY (Category_id) REFERENCES categories (Id)
            )
        """
        cur.execute(sqlite_query)
        connection.commit()


def add_data():
    with sqlite3.connect("vk_chat_bot.db") as connection:
        cur = connection.cursor()
        sqlite_query = """
        INSERT INTO categories (Category_name)
        VALUES ('Выпечка'), ('Кондитерская');"""
        cur.execute(sqlite_query)

        sqlite_query = """
        INSERT INTO items (Item_name, Description)
        VALUES ('Выпечка'), ('Кондитерская');"""
        cur.execute(sqlite_query)

        connection.commit()



# sqlite_query = """
#         INSERT INTO categories (Category_name)
#         VALUES (cытный многозерновой хлеб), (молочно-сливочная булка), (Хлеб с томатами и луковыми чипсами)"""
