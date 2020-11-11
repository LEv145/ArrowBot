"""Частинка бота яка відповідає за базу данних"""

import json

from loguru import logger
import psycopg2


#Завантаження конфіга
with open('lib/bot/config.json', 'r') as f:
	cfg = json.load(f)

class DataBase():
    """Клас який відповідає за базу данних"""
    try:
        conn = psycopg2.connect(user=cfg["POSTGRESQL"]["USER"],
                            password=cfg["POSTGRESQL"]["PASSWORD"],
                            host=cfg["POSTGRESQL"]["HOST"],
                            port=cfg["POSTGRESQL"]["PORT"],
                            database=cfg["POSTGRESQL"]["DATABASE"])

        cur = conn.cursor()

        logger.debug("База данних (PostgreSQL) завантажилася")

    except (Exception, psycopg2.Error) as e:
        logger.error("Не вдалося завантажити базу данних (PostgreSQL):\n{error}", error=e)
    finally:
        if(conn):
            cur.close()
            conn.close()
            logger.info("Підключення до PostgreSQL вимкнено")