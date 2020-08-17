import discord
import random
import asyncio
import datetime
import os
from discord.ext import commands

client = commands.Bot(command_prefix ="g>")
owner = ["194830015353847817"]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(discord.utils.oauth_url(client.user.id))

    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("poggers"))

@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 194830015353847817:
        client.unload_extension(f"Cogs.{extension}")
        client.load_extension(f"Cogs.{extension}")
        await ctx.send("Reloaded succesfully {}, my master.".format(extension))
    else:
        await ctx.send("Not enough Permissions bucko. {}".format(ctx.author.id))



@client.command(pass_context=True, hidden=True)
async def setgame(ctx, *, game):
    if ctx.message.author.id != 194830015353847817:
        return
    game = game.strip()
    if game != "":
        try:
            await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=game))
        except:
            await ctx.send("Failed to change game")
        else:
            await ctx.send("Successfuly changed game to {}".format(game))

for filename in os.listdir("./Cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"Cogs.{filename[:-3]}")






#made by absol#0666



















































client.run("Nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
