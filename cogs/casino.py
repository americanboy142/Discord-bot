from discord.ext.commands import Cog,command
from discord import Client
import itertools, random
import asyncio
import discord
from discord.ext.commands import Bot
import user
import numpy as np

class casino(Cog):
    CARD_SUIT = [':spades:',':diamonds:',':hearts:',':clubs:']
    CARD_NUM = [1,2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    deck = []
   

    def __init__(self,bot):
        self.bot = bot

    def build_deck(self):
        self.deck = []
        self.deck = list(itertools.product(self.CARD_NUM,self.CARD_SUIT))
        random.shuffle(self.deck)

    def cardtoint(self,card):
        if card == 'A':
            return 11
        if card == 'J' or card == 'Q' or card == 'K':
            return 10
        else:
            return card
    
    
    #=====================BLACKJACK===================#
    #get the sum of the hand no print
    def checkHand(self,hand):
        summ = 0
        for i in range(len(hand)):        
            if self.cardtoint(hand[i][0]) == 11:
                try:
                    summ += int(self.cardtoint(hand[i][0]))
                except summ > 21:
                    summ -= 10
            else:
                summ += int(self.cardtoint(hand[i][0]))
        return summ

    #done
    async def printcard(self,ctx,card):
        await ctx.send(str(card[0]) + str(card[1]))
    #done
    async def printhand(self,ctx,hand):
        for i in range(len(hand)):
            await ctx.send(str(hand[i][0]) + str(hand[i][1]))

    #gives the user a requested number of cards
    #converted
    async def hit(self,ctx,hand):
        hand.append((self.deck[self.pick[self.count]][0],self.deck[self.pick[self.count]][1]))
        await self.printhand(ctx,hand)
        self.count+=1
        summ = self.checkHand(hand)
        if summ > 21:
            await ctx.send('bust')
            self.bust = True
        else:
            await ctx.send("Do you want to Hit again(y/n): ")
            try:
                hit = await self.bot.wait_for("message", timeout=20.0)
            except asyncio.TimeoutError:
                await ctx.send("you took to long")
            if hit.content == 'y':
                await self.hit(ctx,hand)
            else:
                return

    #converted
    async def hitdealer(self,ctx,hand):
        hand.append((self.deck[self.pick[self.count]][0],self.deck[self.pick[self.count]][1]))
        await ctx.send("Dealer hand:")
        await self.printhand(ctx,hand)
        self.count+=1
        summ = self.checkHand(hand)
        if summ > 21:
            await ctx.send('bust')
            self.dealbust = True
        elif summ < 16:
            await self.hitdealer(ctx,hand)
        else:
            return

    async def blackdeal(self,ctx):
        self.USER_HAND = []
        self.DEALER_HAND = []
        self.build_deck()
        self.pick=random.sample(range(52), 10)
        self.USER_HAND.append((self.deck[self.pick[0]][0],self.deck[self.pick[0]][1]))
        self.DEALER_HAND.append((self.deck[self.pick[1]][0],self.deck[self.pick[1]][1]))
        self.USER_HAND.append((self.deck[self.pick[2]][0],self.deck[self.pick[2]][1]))
        self.DEALER_HAND.append((self.deck[self.pick[3]][0],self.deck[self.pick[3]][1]))
        self.dealerBlack = False
        self.userBlack = False

        await ctx.send("dealer Hand: ")
        await self.printcard(ctx,self.DEALER_HAND[0])
        await ctx.send("your hand: ")
        await self.printhand(ctx,self.USER_HAND)
        summ = self.checkHand(self.DEALER_HAND)
        if summ == 21:
            self.dealerBlack = True
            await self.printhand(ctx,self.DEALER_HAND)
        summ = self.checkHand(self.USER_HAND)
        if summ == 21:
            self.userBlack = True
            await ctx.send("you have Blackjack!")


    #printcard, print hand , hit, hitdealer, blackdeal
    @command(name="blackjack", aliases = ["bj"])
    async def blackjack(self,ctx,credits):
        if int(credits) > int(user.getCredits(ctx.author)):
            await ctx.send("you dont have that many credits")
        else:
            win = False
            self.count = 4
            self.bust = False
            self.dealbust = False
            await self.blackdeal(ctx)
            #========blackjack=========
            if self.userBlack == True and self.dealerBlack == True:
                await ctx.send("its a tie")
            elif self.userBlack == False and self.dealerBlack == True:
                await ctx.send("you lost")
                user.winlose(ctx.author,credits,False)
            elif self.userBlack == True and self.dealerBlack == False:
                await ctx.send(f"you win {(int(credits)*2)} credits")
                user.winlose(ctx.author,int(credits)*2,True) 
            #==========================
            else:
                print(self.count)
                sumuser = 0
                sumdeal = 0
                #========hit/stay question=========
                await ctx.send("Do you want to Hit or Stay(h/s): ")
                try:
                    hit = await self.bot.wait_for("message", timeout=15.0)
                except asyncio.TimeoutError:
                    await ctx.send("you took to long")
                #========hit/stay again==========
                if hit.content == 'h':
                    await self.hit(ctx,self.USER_HAND)
                    sumuser = self.checkHand(self.USER_HAND)
                #================================
                if sumuser <= 21:
                    await ctx.send("Dealer Hand: ")
                    await self.printhand(ctx,self.DEALER_HAND)
                    sumdeal = self.checkHand(self.DEALER_HAND)
                    if sumdeal > 16:
                        #=========dealer cant hit=============
                        if sumuser > sumdeal:
                            win = True
                        elif sumuser < sumdeal:
                            win = False
                        else:
                            await ctx.send("its a tie")
                        #======================================
                    else:
                        #==============dealer must hit ==============
                        await self.hitdealer(ctx,self.DEALER_HAND)
                        if sumdeal <= 21:
                            if sumuser > sumdeal:
                                win = True
                            elif sumuser < sumdeal:
                                win = False
                            else:
                                await ctx.send("its a tie")
                        else:
                            win = True
                        #==============================================
                    if win == True:
                        await ctx.send(f"you won {credits} credits")
                    if win == False:
                        await ctx.send("you lost")
                    user.winlose(ctx.author,credits,win)
                else:
                    await ctx.send("you lost")
                    user.winlose(ctx.author,credits,False)

    #=========================SLOTS===================#
    SLOT_ITEMS = [(":flag_us:",1),(":diamond_shape_with_a_dot_inside:",4),(":seven:",10),
                  (":peach:",15),(":apple:",21),(":cupcake:",21),(":eggplant:",28)]
    '''
    percentages{
    SLOT_ITEMS[0] = 1 %1    /
    SLOT_ITEMS[1] = 5 %4    /
    SLOT_ITEMS[2] = 13 %7   /
    SLOT_ITEMS[3] = 28 %13  / 
    SLOT_ITEMS[4] = 49 %21  /
    SLOT_ITEMS[5] = 70 %21  /
    SLOT_ITEMS[6] = 100 %33
    }
    '''
    slotpool = []

    def rec_slot(self,count,string):
        if count == 0:
            return 
        else:
            self.slotpool.append(string)
            self.rec_slot((count-1),string)

    def creatslot(self):
        self.slotpool = []
        for i in self.SLOT_ITEMS:
            self.rec_slot(i[1],i[0])
        random.shuffle(self.slotpool)

    def setSlotPos(self,num,vec1):
        vec2 = []
        vec2.append(vec1[num-1])
        vec2.append(vec1[num])
        try:
            vec2.append(vec1[num+1])
        except:
            vec2.append(vec1[0])
        return vec2       

    def slotRoll(self):
        #self.SLOT_ONE = []
        #self.SLOT_THREE = []
        #self.SLOT_TWO = []
        self.SLOT_ONE_POS = []
        self.SLOT_TWO_POS = []
        self.SLOT_THREE_POS = []
        self.creatslot()

        random.shuffle(self.slotpool)
        slotnum = np.random.randint(100)
        self.SLOT_ONE_POS = self.setSlotPos(slotnum,self.slotpool)
        random.shuffle(self.slotpool)
        slotnum = np.random.randint(100)
        self.SLOT_TWO_POS = self.setSlotPos(slotnum,self.slotpool)
        random.shuffle(self.slotpool)
        slotnum = np.random.randint(100)
        self.SLOT_THREE_POS = self.setSlotPos(slotnum,self.slotpool)

    def getBonus(self):
        self.bonus = 0
        self.win = False
        #all three are same
        if self.SLOT_ONE_POS[1] == self.SLOT_TWO_POS[1] == self.SLOT_THREE_POS[1]:
            self.win = True
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[0][0]:
                self.bonus = 5000
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[1][0]:
                self.bonus = 100
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[2][0]:
                self.bonus = 20
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[3][0]:
                self.bonus = 5
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[4][0] or self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[5][0]:
                self.bonus = 3
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[6][0]:
                self.bonus = 1
        #if two are same
        elif self.SLOT_ONE_POS[1] == self.SLOT_TWO_POS[1]:
            self.win = True
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[0][0]:
                self.bonus = 1000
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[1][0]:
                self.bonus = 50
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[2][0]:
                self.bonus = 5
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[3][0]:
                self.bonus = 2
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[4][0] or self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[5][0]:
                self.bonus = 1
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[6][0]:
                self.bonus = 0
        elif self.SLOT_TWO_POS[1] == self.SLOT_THREE_POS[1]:
            self.win = True
            if self.SLOT_TWO_POS[1] == self.SLOT_ITEMS[0][0]:
                self.bonus = 1000
            if self.SLOT_TWO_POS[1] == self.SLOT_ITEMS[1][0]:
                self.bonus = 50
            if self.SLOT_TWO_POS[1] == self.SLOT_ITEMS[2][0]:
                self.bonus = 5
            if self.SLOT_TWO_POS[1] == self.SLOT_ITEMS[3][0]:
                self.bonus = 2
            if self.SLOT_TWO_POS[1] == self.SLOT_ITEMS[4][0] or self.SLOT_TWO_POS[1] == self.SLOT_ITEMS[5][0]:
                self.bonus = 1
            if self.SLOT_TWO_POS[1] == self.SLOT_ITEMS[6][0]:
                self.bonus = 0
        elif self.SLOT_ONE_POS[1] == self.SLOT_THREE_POS[1]:
            self.win = True
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[0][0]:
                self.bonus = 1000
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[1][0]:
                self.bonus = 50
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[2][0]:
                self.bonus = 5
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[3][0]:
                self.bonus = 2
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[4][0] or self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[5][0]:
                self.bonus = 1
            if self.SLOT_ONE_POS[1] == self.SLOT_ITEMS[6][0]:
                self.bonus = 0
        #if none are same
        else:
            self.bonus = 0

    @command(name="slots",aliases = ["slot"])
    async def slots(self,ctx,credits):
        if int(credits) > int(user.getCredits(ctx.author)):
            await ctx.send("you dont have that many credits")
        else:
            user.takeCredits(ctx.author,credits)
            self.bonus = 0
            ctx.send(f"Slots for {credits} credits")
            self.slotRoll()
            for i in range(3):
                await ctx.send(self.SLOT_ONE_POS[i] + self.SLOT_TWO_POS[i] + self.SLOT_THREE_POS[i])
            self.getBonus()
            user.winlose(ctx.author,int(credits) * self.bonus, True)
            if self.bonus > 0:
                await ctx.send(f"you won {int(self.bonus) * int(credits)} credits!")
            else:
                await ctx.send(f"you lost {credits} credits")
        
            
    #=======================coinflip===================
    @command(name="flip")
    async def flip(self,ctx,guess,credits):
        if int(credits) > int(user.getCredits(ctx.author)):
            await ctx.send("you dont have that many credits")
        else:
            result = np.random.randint(2)
            if guess == 'heads' or guess == 'h' or guess == 'head':
                guess == '0'
                valid = True
            elif guess == 'tails' or guess == 't' or guess == 'tail':
                guess == '1'
                valid = True
            else:
                await ctx.send("not valid guess")
                await ctx.send("example: flip h 20")
                valid = False
            if valid == True:
                if result == int(guess):
                    await ctx.send(f"you won {credits} credits")
                    user.winlose(ctx.author,credits,True)
                else:
                    await ctx.send(f"you lost")
                    user.winlose(ctx.author,credits,False)
            await ctx.send(f"you have {user.getCredits(ctx.author)} credits")

    #===========================DICEROLL======================
    @command(name="roll")
    async def roll(self,ctx,guess,credits):
        if int(credits) > int(user.getCredits(ctx.author)):
            await ctx.send("you dont have that many credits")
        else:
            actual = np.random.randint(6)
            if guess == actual:
                await ctx.send(f"you won {int(credits) * 6}")
                user.winlose(ctx.author,int(credits) * 6,True)
            else:
                user.winlose(ctx.author,int(credits) * 6,False)

            
                

def setup(bot):
    bot.add_cog(casino(bot))