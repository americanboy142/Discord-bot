import itertools, random
import numpy as np

from discord.enums import UserContentFilter

def makeDeck():
    deck = []
    for i in range(4):
        for i in range(1, 14):
            deck.append(i)
    return(deck)

def shuffle(decks):
    deck = []
    for i in range(decks):
        deck.append(makeDeck())
    return(random.shuffle(deck))

class BlackJack:
    userCards =[]
    dealerCards = []

    def __init__(self,decks):
        self.userCards.append(random.sample(decks, 1))
        self.dealerCards.append(random.sample(decks, 1))
        self.userCards.append(random.sample(decks, 1))
        self.dealerCards.append(random.sample(decks, 1))
        #return (self.userCards,self.dealerCards)

    def hit(self,decks):
        self.userCards.append(random.sample(decks, 1))

    def add(self,hand):
        summ = 0
        ace = False
        for card in hand:
            if (card == 'J' or card == 'Q' or card == 'K'):
                card = '10'
            elif(card == 'A'):
                card = '11'
                ace = True
            if ace == True
            summ = summ + int(card)

    def dealer(self,decks):

        self.dealerCards.append(random.sample(decks, 1))



def checkForFace(card):
    if(card == 1):
        return 'A'
    if card == 11:
        return 'J'
    if card == 12:
        return 'Q'
    if card == 13:
        return 14
    return card
