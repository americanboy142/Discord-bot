from discord.ext.commands import Cog,command
import asyncio
import config
import tinder_api_sms
import user
import mainTinder

class tinder(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="setToken", aliases = ["settoken"])
    async def setToken(self,ctx):
        thing = user.checkToken(ctx.author)
        if(thing[0] == False):
            await ctx.send("you dont have a token")
            await ctx.send("enter Tinder Token:")
            try:
                    answer = await self.bot.wait_for("message", timeout=15.0)
            except asyncio.TimeoutError:
                await ctx.send("you took to long")
            config.addToken(ctx.author, answer.content)
        else:
            tinder_api_sms.tinder_token = thing[1]
            await ctx.send("using " + str(ctx.author) + "'s Tinder")


    @command(name="Tinder", aliases = ["tinder"])
    async def tinder(self,ctx):
        user.check(ctx.author)
        try:
            while(True):
                deal = 'dislike'
                info = mainTinder.getInfo()
                '''
                info = {
                    photos, name , age , bio ,person_id
                }
                '''
                #print("after")
                await ctx.send(info[0][0])
                await ctx.send(str(info[1]) + ": " + str(info[2]))
                try:
                    await ctx.send(info[3])
                except:
                    await ctx.send("she dont got a bio unlucky")
                await ctx.send("Like or Dislike?")
                #print(person)
                try:
                    answer = await self.bot.wait_for("message", timeout=15.0)
                    print(answer.content.lower())
                    print(type(answer.content))
                except asyncio.TimeoutError:
                    await ctx.send("you is too picky")
                    break
        
                if answer.content.lower() == 'like' or answer.content.lower() == 'right':
                    deal = "like"
                elif answer.content.lower() == 'dislike' or answer.content.lower() == 'left':
                    deal = "dislike"
                elif answer.content.lower() == 'done':
                    await ctx.send("exit")
                    break
                else:
                    await ctx.send("you just broke her how dare you")
                    break

                # MATCH STUFF AND LIKING
                person = info[4]
                if deal == "like":
                    tinder_api_sms.like(person)
                    await ctx.send("liked")
                    matchInfo = mainTinder.checkIfMatch(person)
                    match = matchInfo[1]
                    matchId = matchInfo[0]
                    if match == True:
                        await ctx.send("https://c.tenor.com/9VuG1d2QOOQAAAAM/oh-my-god-its-happening.gif")
                        await ctx.send("this is so huge you match with a female you must be good lookin.")
                        await ctx.send("would you like to send a message(y/n):")
                        try:
                            answer = await self.bot.wait_for("message", timeout=15.0)
                        except asyncio.TimeoutError:
                            await ctx.send("you took to long")
                            break
                        if answer.content == 'y':
                            await ctx.send("Type message:")
                            try:
                                msg = await self.bot.wait_for("message", timeout=15.0)
                            except asyncio.TimeoutError:
                                await ctx.send("you took to long")
                                break
                            try:
                                tinder_api_sms.send_msg(matchId,msg.content)
                                await ctx.send("message sent she wants the goods")
                            except:
                                await ctx.send("message not sent sorry")
                        else:
                            await ctx.send("how dare you its fate you punk kid")
                    else:
                        await ctx.send("you didnt match thats ok you will get him next time.")
                    #break
                else:
                    tinder_api_sms.dislike(person)
                    await ctx.send("disliked")
                    #break
        except:
            await ctx.send("tinder token not valid")


    @command(name="dms", aliases = ["message"])
    async def dms(self,ctx):
        matches = tinder_api_sms.all_matches()['data']['matches']
        for match in matches:
            matchPhotos = []
            photos = match['person']['photos']
            for photo in photos:
                matchPhotos.append(photo['url'])
            matchId = match['_id']
            matchName = match['person']['name']
            try:
                matchBio = match['person']['bio']
            except:
                matchBio = "she shant have a bio so"
            await ctx.send(matchPhotos[0])
            await ctx.send(str(matchName))
            await ctx.send(str(matchBio))

            # ask if more photos or is good
            await ctx.send("=========================================================")
            await ctx.send("(y/n) to send message. (more) to see more photos. (done) to stop playing")
            try:
                answer = await self.bot.wait_for("message", timeout=15.0)
            except asyncio.TimeoutError:
                await ctx.send("you took to long")
                break
            if answer.content == 'done':
                await ctx.send("exited")
                break
            elif answer.content == 'm' or answer.content == 'more':
                # loop for photos
                for photo in matchPhotos:
                    await ctx.send(photo)
                await ctx.send("Now would you like to send your girl a message(y/n):")
                try:
                    answer = await self.bot.wait_for("message", timeout=15.0)
                except asyncio.TimeoutError:
                    await ctx.send("you took to long")
                    break
                # re-ask if message
                if answer.content == 'y':
                    await ctx.send("Type message:")
                    try:
                        msg = await self.bot.wait_for("message", timeout=15.0)
                    except asyncio.TimeoutError:
                        await ctx.send("you took to long")
                        break
                    try:
                        tinder_api_sms.send_msg(matchId,msg.content)
                        await ctx.send("message sent she wants the goods")
                    except:
                        await ctx.send("message not sent sorry")
                if answer.content == 'n':
                    await ctx.send("you think you to good or somthing")
            else:
                if answer.content == 'y':
                    await ctx.send("Type message:")
                    try:
                        msg = await self.bot.wait_for("message", timeout=15.0)
                    except asyncio.TimeoutError:
                        await ctx.send("you took to long")
                        break
                    try:
                        tinder_api_sms.send_msg(matchId,msg.content)
                        await ctx.send("message sent she wants the goods")
                    except:
                        await ctx.send("message not sent sorry")
                if answer.content == 'n':
                    await ctx.send("you think you to good or somthing")
                if answer.content == 'done':
                    await ctx.send("exited")
                    break

def setup(bot):
    bot.add_cog(tinder(bot))