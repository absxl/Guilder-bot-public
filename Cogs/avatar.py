import discord
import random
import time
import asyncio
import datetime

from discord import DMChannel
from discord.ext import commands
from discord.utils import get


class avatar(commands.Cog):

    def __init__(self, client):
        self.client = client






    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        """User Avatar"""
        await ctx.send("{}".format(member.avatar_url))



def setup(client):
    client.add_cog(avatar(client))





# made by absol (absol#0666)
