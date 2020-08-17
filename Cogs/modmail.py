import discord
import random
import time
import asyncio
import datetime

from discord import DMChannel
from discord.ext import commands
from discord.utils import get


class modmail(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
    		if not message.author.bot:
    			if isinstance(message.channel, DMChannel):
    				if len(message.content) < 49 or len(message.content) > 1025:
    					await message.channel.send("Your message should be long between 50 characters and 1024 characters in length.")

    				else:
    					member = self.client.get_user(message.author.id)
    					embed = discord.Embed(title="Modmail",
    								  colour=member.colour)

    					embed.set_thumbnail(url=member.avatar_url)

    					fields = [("Member", member.display_name, False),
    							  ("Message", message.content, False)]

    					for name, value, inline in fields:
    						embed.add_field(name=name, value=value, inline=inline)

    					logs = self.client.get_channel(742567426759196723)
    					await logs.send(embed=embed)
    					await message.channel.send("Message relayed to moderators, the only approved moderators are absol#0666 and Ferry#1042.")

    			else:
    				return




def setup(client):
    client.add_cog(modmail(client))





# made by absol (absol#0666)
