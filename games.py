import itertools, random

from discord.enums import UserContentFilter

def makeDeck():
    deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

def shuffle(decks):
    deck = []
    for i in range(decks):
        deck.append(makeDeck())
    return(random.shuffle(deck))

class blackjack():
    def deal(decks):
        userCards =[]
        dealerCards = []
        userCards.append(random.sample(decks, 1))
        dealerCards.append(random.sample(decks, 1))
        userCards.append(random.sample(decks, 1))
        dealerCards.append(random.sample(decks, 1))
        return (userCards,dealerCards)


