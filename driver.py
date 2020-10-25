from sqlite3 import *
from os import path


class DbDriver(object):
    def __init__(self):
        self._db_path = path.abspath('univer.db')
        self._conn = connect(self._db_path)
        self._cursor = self._conn.cursor()

    def execute_dml(self, query: str, params: tuple) -> None:  # data manipulation language
        if len(params) == 0:
            self._cursor.execute(query)
        else:
            self._cursor.execute(query, params)
        self._conn.commit()

    def execute_select(self, query: str, params: tuple) -> list:
        if len(params) == 0:
            result = self._cursor.execute(query)
        else:
            result = self._cursor.execute(query, params)
        return result.fetchall()
