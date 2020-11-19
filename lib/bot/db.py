"""Частинка бота яка відповідає за базу данних"""

import json
from os.path import isfile
import atexit

from loguru import logger
import psycopg2


BUILD_PACH = "data/db/build.sql"

#Завантаження конфіга
with open("lib/bot/config.json", "r") as f:
	cfg = json.load(f)

#Завантаження бази данних
conn = psycopg2.connect(user=cfg["POSTGRESQL"]["USER"],
                    password=cfg["POSTGRESQL"]["PASSWORD"],
                    host=cfg["POSTGRESQL"]["HOST"],
                    port=cfg["POSTGRESQL"]["PORT"],
                    database=cfg["POSTGRESQL"]["DATABASE"])

cursor = conn.cursor()
logger.debug("База данних (PostgreSQL) завантажилася")


def with_commit(func):
    """Функція яка відповідає за підтвердження"""
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        conn.commit()

    return inner

@with_commit
def build():
    """Функція яка відповідає за побудову таблиці"""
    if isfile(BUILD_PACH):
        load_script(BUILD_PACH)

def load_script(pach):
    """Функція яка відповідає за завантаження скриптів"""
    cursor.execute(open(pach, "r", encoding="utf-8").read())

def exit_conn():
    """Функція яка вимикає підключення до бази данних, під час вимкнення бота"""
    if(conn):
        cursor.close()
        conn.close()
        logger.info("Підключення до PostgreSQL вимкнено")

atexit.register(exit_conn)