"""Частинка бота яка відповідає за роботу бота"""

import json

import discord
from discord.ext import commands
from loguru import logger

from . import db
from . import utils


#Завантаження конфіга
with open("data/config.json", "r", encoding="utf-8") as f:
	cfg = json.load(f)

#Список ID розробників бота
OWNER_IDS = [
    "411885690993901588"
]

#Список всіх когів
COGS_LIST = [
    "lib.cogs.event",
]

#Інформація про бота
BOT_DESC = "ArrowBot by Videf"

def get_prefix(bot, message):
    """Функція яка відповідає за префікс"""
    db.cursor.execute(f"SELECT Prefix FROM guilds WHERE GuildID = {message.guild.id}")
    prefix = db.cursor.fetchone()

    return prefix

class WorkerBot(commands.Bot):
    """Клас який відповідає за роботу бота"""
    def __init__(self):
        logger.debug("Завантаження головних параметрів")
        super().__init__(command_prefix=get_prefix,
                    intents=discord.Intents.all(),
                    case_insensitive=True,
                    owner_ids=OWNER_IDS,
                    description=BOT_DESC)

    def load_cog(self):
        """Функція яка відповідає за завантаження когів"""
        for cogs_list in COGS_LIST:
            try:
                self.load_extension(cogs_list)
                logger.debug("Завантажився {cog}", cog=cogs_list)
            except Exception as e:
                logger.error("Не вдалося завантажити {cog}:\n {error}", cog=cogs_list, error=e)

    def run(self):
        """Функція яка відповідає за запуск бота"""
        logger.debug("Завантаження когів")
        self.load_cog()
        
        logger.debug("Підключення до таблиці бази данних")
        db.build()

        logger.debug("Завантаження токена")
        with open("lib/bot/private_config.json", "r", encoding="utf-8") as f:
            self.BOT_TOKEN = json.load(f)

        logger.debug("Підключення токена")
        logger.debug("==========================================")
        super().run(self.BOT_TOKEN["BOT"]["TOKEN"], reconnect=True)

    async def on_ready(self):
        """Функція яка викликається при готовності бота"""
        guilds = await self.fetch_guilds(limit=None).flatten()
        members = len(set(self.get_all_members()))

        logger.debug("Завантаження статусу")
        await self.change_presence(status=discord.Status.online,
                                activity=discord.Activity(name=f"за {len(guilds)} серверами",
                                            type=discord.ActivityType.watching))

        #Вивод інформації про бота в консоль
        logger.debug("{name} запустився", name=self.user.name)
        logger.debug("Версія бота: {version}", version=cfg["BOT"]["VERSION"])
        logger.debug("Бот знаходиться на {guild} серверах", guild=len(guilds))
        logger.debug("Обробляю {member} користувачів", member=members)
        logger.debug("==========================================")

bot = WorkerBot()