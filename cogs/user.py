from discord.ext.commands import Cog,command
import user
from discord.ext.commands import CommandOnCooldown
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands.core import cooldown

class User(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="credits")
    async def credits(self, ctx):
        user.check(ctx.author)
        await ctx.send(f"{ctx.author.mention} you have {str(user.getCredits(ctx.author))}  credits")

    @command(name="daily")
    @cooldown(1,60*24,BucketType.user)
    async def daily(self, ctx):
        try:
            user.giveCredits(ctx.author)
            await ctx.send(f"{ctx.author.mention} you have {str(user.getCredits(ctx.author))}  credits")
        except :
            await ctx.send("on cooldown")
    



def setup(bot):
    bot.add_cog(User(bot))