"""Частинка бота яка відповідає за базу данних"""

from loguru import logger
import psycopg2


#Завантаження бази данних
try:
    conn = psycopg2.connect(user="",
                        password="",
                        host="",
                        port="",
                        database="")

    cur = conn.cursor()

    logger.debug("База данних (PostgreSQL) завантажилася")

except (Exception, psycopg2.Error) as e:
    logger.error("Не вдалося завантажити базу данних (PostgreSQL):\n{error}", error=e)
finally:
    if(conn):
        cur.close()
        conn.close()
        logger.info("Підключення до PostgreSQL вимкнено")