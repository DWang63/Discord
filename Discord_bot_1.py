import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time

client = discord.Client()
bot_command = commands.Bot(command_prefix = "d!")
#this is to choose something that the bot will respond too, like for example "d! play" would be a command


@client.event
async def on_ready():
    print ("Bot is Ready!")

@client.event
async def on_message(message):
    if message.content.startwith("d! hello"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s Hello there!" % (userID))

client.run("SkgyJH4W4elV0p7Udl-sHxm3ivViA-b_")
#this is a code that you get from the discord website that lets you control a specific bot, kind of like the key

