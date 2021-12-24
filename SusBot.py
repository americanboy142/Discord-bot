import discord
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands.core import Command, cooldown
from maya.core import MayaInterval
import numpy as np
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import CommandOnCooldown
from discord.voice_client import VoiceClient
import asyncio
from discord import Client
#import youtube_dl

import config
import tinder_api_sms
import user
import json
import games

fileName = 'users.json'


client = discord.Client()
bot = commands.Bot(command_prefix='.')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def flip(message):
    result = np.random.randint(2)
    if result == 1:
        await message.channel.send('heads')
    if result == 2:
        await message.channel.send('heads')

'''
class Tinder(commands.cog):
    def __init__(self, bot):
        self.bot = bot
'''
@bot.command()
async def check(ctx):
    user.check(ctx.author)

@bot.command()
async def setToken(ctx):
    thing = user.checkToken(ctx.author)
    if(thing[0] == False):
        await ctx.send("you dont have a token")
        await ctx.send("enter Tinder Token:")
        try:
                answer = await bot.wait_for("message", timeout=15.0)
        except asyncio.TimeoutError:
            await ctx.send("you took to long")
        config.addToken(ctx.author, answer.content)
    else:
        tinder_api_sms.tinder_token = thing[1]
        await ctx.send("using " + str(ctx.author) + "'s Tinder")

@bot.command()
async def tinder(ctx):
    import mainTinder
    user.check(ctx.author)
    #config.setToken(ctx.author)
    #print("befor")
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
            await ctx.send("like or dislike?")
            print(person)
            try:
                answer = await bot.wait_for("reaction", timeout=15.0)
                print(answer.content.lower())
                print(type(answer.content))
            except asyncio.TimeoutError:
                await ctx.send("you is too picky")
                break
        
            if (answer.content.lower()) == 'right' or answer.content.lower() == 'like':
                deal = "like"
            elif (answer.content.lower() == 'left' or answer.content.lower() == 'dislike'):
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
                        answer = await bot.wait_for("message", timeout=15.0)
                    except asyncio.TimeoutError:
                        await ctx.send("you took to long")
                        break
                    if answer.content == 'y':
                        await ctx.send("Type message:")
                        try:
                            msg = await bot.wait_for("message", timeout=15.0)
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


@bot.command()
async def dms(ctx):
    import mainTinder
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
            answer = await bot.wait_for("message", timeout=15.0)
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
                answer = await bot.wait_for("message", timeout=15.0)
            except asyncio.TimeoutError:
                await ctx.send("you took to long")
                break
            # re-ask if message
            if answer.content == 'y':
                await ctx.send("Type message:")
                try:
                    msg = await bot.wait_for("message", timeout=15.0)
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
                    msg = await bot.wait_for("message", timeout=15.0)
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




@bot.command()
async def credits(ctx):
    user.check(ctx.author)
    await ctx.send("you have " + str(user.getCredits(ctx.author)) + " credits")

@bot.command()
@cooldown(1,60*24,BucketType.user)
async def daily(ctx):
    try:
        user.giveCredits(ctx.author)
        await ctx.send("you have " + str(user.getCredits(ctx.author)) + " credits")
    except :
        await ctx.send("on cooldown")
    
@bot.command()
async def hdy(ctx):
    await ctx.send("HOW DARE YOUUUUU")
    await ctx.send("https://www.youtube.com/watch?v=yUGxDF7nYQ8")

@bot.command()
async def ree(ctx):
    await ctx.send("REEEEEEEEEEEEE")
    await ctx.send("https://www.youtube.com/watch?v=2TWdraO9S_M")


@bot.command()
async def blackjack(ctx,credits):
    deck = games.shuffle(3)
    goods = games.backjack.deal(deck)
    user = goods[0]
    dealer = goods[1]
    await ctx.send("Dealer: " + str(dealer[1][0]) + str(dealer[1][1]))
    await ctx.send("your cards: " + str(user[0][0]) + str(user[0][1]) + str(user[1][0]) + str(user[1][1]))





bot.run("NzE5Nzk3OTI3NDA0MzcyMDEw.Xt8qDw.9LqUxLs4hE8qrEvGWP_IubYHEPE")
