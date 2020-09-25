import numpy as np

deck = ()

for i in range(4):
    for i in range(1, 14):
        cvalue = i
        deck = np.append(deck, cvalue)

#spades = np.arange(13)
#clubs = np.arange(13)
##diamonds = np.arange(13)
hiddenDealer = []
hiddenPlayer = []
dealerHand = []
playerHand = []
for i in range(2):
    dealerpick = np.random.choice(deck)
    hiddenDealer = np.append(hiddenDealer, dealerpick)
    if dealerpick == 11:
        dealerHand = np.append(dealerHand, 'J')
    elif dealerpick == 12:
        dealerHand = np.append(dealerHand, 'Q')
    elif dealerpick == 13:
        dealerHand = np.append(dealerHand, 'K')
    else:
        dealerHand = np.append(dealerHand, dealerpick)

playerHand = []

for i in range(2):
    playerpick = np.random.choice(deck)
    hiddenPlayer = np.append(hiddenPlayer, playerpick)
    if playerpick == 11:
        playerHand = np.append(playerHand, 'J')
    elif playerpick == 12:
        playerHand = np.append(playerHand, 'Q')
    elif playerpick == 13:
        playerHand = np.append(playerHand, 'K')
    else:
        playerHand = np.append(playerHand, playerpick)


def hit():
    for i in range(1):
        playerpick = np.random.choice(deck)
        hiddenPlayer = np.append(hiddenPlayer, playerpick)
        if playerpick == 11:
            playerHand = np.append(playerHand, 'J')
        elif playerpick == 12:
            playerHand = np.append(playerHand, 'Q')
        elif playerpick == 13:
            playerHand = np.append(playerHand, 'K')
        else:
            playerHand = np.append(playerHand, playerpick)







def deal():
    print(dealerHand)
    print(playerHand)
    print(hiddenDealer)
    print(hiddenPlayer)





def blackjack():
    hit = input("Hit or Stay?")
    if hit == 'hit':
        hit()
    deal()


blackjack()

