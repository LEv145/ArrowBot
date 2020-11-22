"""Частинка бота яка відповідає за всі події бота"""

import json

from discord.ext import commands
from loguru import logger

from ..bot.db import cursor, conn


#Завантаження конфіга
with open('data/config.json', 'r', encoding="utf-8") as f:
	cfg = json.load(f)

class Event(commands.Cog):
    """Клас який відповідає за всі події"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """Функція яка викликається при вході бота на новий сервер"""
        logger.debug("Я був добавлений на новий сервер: {server}", server=guild.name)
        cursor.execute(f"SELECT GuildID FROM guilds WHERE GuildID = {guild.id}")
        row = cursor.fetchone()
        if row is None:
            cursor.execute(f"INSERT INTO guilds (GuildID, LangBot, LangCom, EmbedColor) VALUES (%s, %s, %s, %s)",
            (guild.id, "english", "english", cfg["EMBED"]["DEFAULT_COLOR"]))
            conn.commit()
        else:
            pass
    

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        """Функція яка викликається при виході бота з сервера"""
        logger.debug("Я був видалений з сервера: {server}", server=guild.name)
        cursor.execute(f"DELETE FROM guilds WHERE GuildID = {guild.id}")
        conn.commit()


def setup(bot):
	"""Добавлення кога"""
	bot.add_cog(Event(bot))