import sqlite3


class QueryItem:
    def __init__(self, item_name, condition):
        self.category_pk = condition - 2

        if item := self._get_item_name(item_name):
            self.item_name = item_name
            self.description = item[2]
            self.link = item[4]
        else:
            self.item_name = None
            self.description = None
            self.link = None

    def __repr__(self):
        return f"{self.item_name}"

    def __bool__(self):
        if self.item_name:
            return True
        return False

    def _get_item_name(self, item_name):
        with sqlite3.connect("db/vk_chat_bot.db") as connection:
            cur = connection.cursor()
            sqlite_query = """
                SELECT *
                FROM items
                WHERE item_name = ?
                AND category_id = ?"""
            cur.execute(sqlite_query, (item_name, self.category_pk))
            return cur.fetchone()


class QueryCategory:
    def __init__(self, category_name, condition):
        if category := self._get_category_name(category_name):
            self.category_name = category_name
            self.category_pk = category[0]
            self.condition = condition + self.category_pk
        else:
            self.category_name = None
            self.category_pk = None

    def __repr__(self):
        return f"{self.category_name}"

    def __bool__(self):
        if self.category_name:
            return True
        return False

    def _get_category_name(self, category_name):
        with sqlite3.connect("db/vk_chat_bot.db") as connection:
            cur = connection.cursor()
            sqlite_query = """
                SELECT *
                FROM categories
                WHERE category_name = ?"""
            cur.execute(sqlite_query, (category_name,))
            return cur.fetchone()
