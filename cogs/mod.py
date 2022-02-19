from discord.ext.commands import Cog,command

class Mod(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="clean", aliases = ["purge","clear"])
    async def clean(self, ctx, amount):
        if 0 < int(amount) <= 100:
            with ctx.channel.typing():
                await ctx.message.delete()
                deleted = await ctx.channel.purge(limit = int(amount))
                await ctx.send(f"Deleted {len(deleted):,} messages.", delete_after=5)
        else:
            await ctx.send("Max is 100 stupid")



def setup(bot):
    bot.add_cog(Mod(bot))