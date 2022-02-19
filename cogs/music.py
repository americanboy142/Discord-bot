from discord.ext.commands import Cog,command
from discord.ext import commands,tasks
from discord.voice_client import VoiceClient
import discord
import os
import youtube_dl

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
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
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename



class music(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name='leave', help='To make the bot leave the voice channel')
    async def leave(self,ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")

    @command(name='play', aliases = ["p"])
    async def play(self,ctx,url):
        #try :
        if not ctx.message.author.voice:
            await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
            return
        else:
            channel = ctx.message.author.voice.channel
            await channel.connect()
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=self.bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
       # except:
       #    await ctx.send("The bot is not connected to a voice channel.")


    @command(name='pause', help='This command pauses the song')
    async def pause(self,ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.pause()
        else:
            await ctx.send("The bot is not playing anything at the moment.")
    
    @command(name='resume', help='Resumes the song')
    async def resume(self,ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_paused():
            await voice_client.resume()
        else:
            await ctx.send("The bot was not playing anything before this. Use play_song command")

    @command(name='stop', help='Stops the song')
    async def stop(self,ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.stop()
        else:
            await ctx.send("The bot is not playing anything at the moment.")


    @command(name="how dare you", aliases = ["hdy"])
    async def hdy(self, ctx):
        await ctx.send("HOW DARE YOUUUUU")
        await self.play(ctx,"https://www.youtube.com/watch?v=yUGxDF7nYQ8")

    @command(name="ree", aliases = ["reeee"])
    async def ree(self, ctx):
        await ctx.send("REEEEEEEEEEEEE")
        await self.play(ctx,"https://www.youtube.com/watch?v=2TWdraO9S_M")


def setup(bot):
    bot.add_cog(music(bot))