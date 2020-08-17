import discord
import random
import time
import asyncio
import datetime

from discord import DMChannel
from discord.ext import commands
from discord.utils import get


class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client





    @commands.command()
    @discord.ext.commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount = None):
        await ctx.channel.purge(limit=amount)
        confirm = await ctx.send("{m} messages purged by {u}".format(u=user.mention, m=amount))
        await asyncio.sleep(7)
        confirm.delete

    @commands.command()
    async def purge (self, ctx, amount=10):
        if ctx.author.id == 194830015353847817:
            user = ctx.author
            await ctx.channel.purge(limit=amount)
            confirm = await ctx.send("{m} messages purged by {u}".format(u=user.mention, m=amount))
            await asyncio.sleep(7)
            confirm.delete


def setup(client):
    client.add_cog(Mod(client))





# made by absol (absol#0666)
