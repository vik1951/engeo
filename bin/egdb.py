# -*- coding: utf-8 -*-
import psycopg2

class ConnectionError(Exception):
    pass


class UseDatebase:
    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> "cursor":
        try:
            self.conn = psycopg2.connect(**self.configuration)
            self.curs = self.conn.cursor()
            return self.curs
        except psycopg2.DatabaseError as err:
            raise ConnectionError(err)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.curs.close()
        self.conn.close()
