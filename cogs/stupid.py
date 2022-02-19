from discord.ext.commands import Cog,command
import numpy as np

class Stupid(Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @command(name="ping")
    async def ping(self, ctx):
        await ctx.send('pong')


    @command(name="coinflip")
    async def coinflip(self, ctx):
        result = np.random.randint(2)
        if result == 0:
            await ctx.channel.send('heads')
        if result == 1:
            await ctx.channel.send('heads')


def setup(bot):
    bot.add_cog(Stupid(bot))