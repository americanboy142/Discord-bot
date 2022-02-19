import discord
#from discord.ext.commands.cooldowns import BucketType
#from discord.ext.commands.core import Command, cooldown
#from maya.core import MayaInterval
#import numpy as np
from discord.ext import commands
#from discord.ext.commands import Bot
#from discord.ext.commands import CommandOnCooldown
#from discord.voice_client import VoiceClient
#import asyncio
#from discord import Client
#from requests.api import delete
from pretty_help import DefaultMenu, PrettyHelp
#import youtube_dl

#import games

fileName = 'users.json'


client = discord.Client()
bot = commands.Bot(command_prefix='.')

bot.load_extension("cogs.stupid")
bot.load_extension("cogs.user")
bot.load_extension("cogs.mod")
bot.load_extension("cogs.redit")
bot.load_extension("cogs.casino")
bot.load_extension("cogs.tinder")
bot.load_extension("cogs.music")
print("all loaded")


menu = DefaultMenu('prev', 'next', 'exit')
bot.help_command = PrettyHelp(navigation=menu, color=discord.Colour.red()) 




bot.run("##discord Tocken##")
