"""Частинка бота яка відповідає за команди модерації"""

import json

import discord
from discord.ext import commands


#Завантаження конфіга
with open('data/config.json', 'r') as f:
	cfg = json.load(f)

class Moderation(commands.Cog, name="Модерація"):
    """Головний клас команд модерації"""
    def __init__(self, bot):
        self.bot = bot
        self.EMB_BASIC_COLOR = cfg["EMB"]["BASIC_COLOR"]

    @commands.command(name="заблокувати",
                aliases=["бан"],
                description="Команда <Заблокувати>, блокує указаного користувача на сервері",
                brief="Блокує указаного користувача",
                usage="заблокувати <@користувач> <причина>")
    @commands.has_permissions(ban_members=True)
    async def ban_command(self, ctx, member:discord.Member=None, *, reason=None):
        """Команда <Заблокувати>, блокує указаного користувача на сервері"""
        ping = ctx.message.author.mention
        if member is None:
            return await ctx.send(f"{ping}, укажіть користувача :broccoli:")
        elif member.id == ctx.author.id:
            return await ctx.send(f"{ping}, неможна заблокувати самого себе :cactus:")
        elif ctx.author.top_role.position < member.top_role.position:
            return await ctx.send(f"{ping}, неможна заблокувати користувача який вище вас за ролью :beetle:")
        elif member.id == ctx.guild.owner.id:
            return await ctx.send(f"{ping}, неможна заблокувати творця сервера :deciduous_tree:")
        if reason is None:
            await member.send(f"Вас було заблоковано на сервері **{ctx.guild.name}**, модератором **{ctx.author.name}**")
            embed = discord.Embed(color=int(self.EMB_BASIC_COLOR, 16),
                        description=f"Користувач **{member}** був заблокований на сервері, модератором **{ctx.author.name}**")
            await member.ban()
            return await ctx.send(embed=embed)
        else:
            await member.send(f"Вас було заблоковано на сервері **{ctx.guild.name}**, модератором **{ctx.author.name}**\nПо причині: **{reason}**")
            embed = discord.Embed(color=int(self.EMB_BASIC_COLOR, 16),
                        description=f"Користувач **{member}** був заблокований на сервері, модератором **{ctx.author.name}**\nПо причині: **{reason}**")
            await member.ban()
            return await ctx.send(embed=embed)
        
def setup(bot):
	"""Добавлення кога"""
	bot.add_cog(Moderation(bot))