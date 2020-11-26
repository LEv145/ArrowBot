"""Частинка бота яка відповідає за всі корисні можливості"""

import sys

from loguru import logger

#Конфіг для відображення логів
log_config = {
    "handlers": [
        {"sink": sys.stdout, "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level}</level> | <level>{message}</level>"}
    ]
}

logger.configure(**log_config)

#Запис логів в файлик
logger.add("data/log/debug.log", format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {message}",
level="DEBUG", rotation="10 MB", compression="zip")