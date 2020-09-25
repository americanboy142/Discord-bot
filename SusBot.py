import discord
import numpy as np
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from discord import Client
from discord.ext import commands
import youtube_dl

client = discord.Client()
bot = commands.Bot(command_prefix='.')

youtube_dl.utils.bug_reports_message = lambda: ''
players = {}

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')


@client.event
async def on_ready():
    print('online')


@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("penis"):
        await message.channel.send("penis!")
    if message.content == 'ping':
        await message.channel.send('pong')
    if message.content == 'how':
        await asyncio.sleep(1)
        await message.channel.send('dare')
        await asyncio.sleep(1)
        await message.channel.send('UUUUUUUU')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

class Music(commands.cog):
    def __init__(self, bot):
        self.bot = bot
    @bot.command()
    async def join(ctx):
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
        else:
            await ctx.send("You are not connected to a voice channel.")
            return
        global vc
        try:
            vc = await channel.connect()
        except:
            TimeoutError


    @bot.command()
    async def leave(ctx):
        guild = ctx.message.guild
        voice_client = guild.voice_client
        await voice_client.disconnect()


    @bot.command()
    async def flip(message):
        result = np.random.randint(2)
        if result == 1:
            await message.channel.send('heads')
        if result == 2:
            await message.channel.send('heads')


    @bot.command()
    async def stream(ctx, url):
        async with ctx.typing():
            player = await YTDLSource.from_url(url)
            ctx.voice_client.play(player)

        await ctx.send('Now playing: {}'.format(player.title))

client.run("NzE5Nzk3OTI3NDA0MzcyMDEw.Xt_Ydg.OfJmj7IEwIYtHiUIZtYG_8oH3GE")
