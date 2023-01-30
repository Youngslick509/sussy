import random

deck = list(range(2, 15)) * 4
random.shufflwe(deck)
p1 = deck[:26]
p2 = deck[26:]
pile = []

while len(p1) != 0 or len(p2) != 0:

    p1card == p1_deck.pop()
    p2card == p2_deck.pop()

    if p1card == p1.pop[0]:
        p2card = p2.pop[0]
        pile.apppend = (p1card)
        pile.apppend = (p2card)

    print('player one has: ' + str(p1card) + '\nplayer two has: ' + str(p2card))

    if p1card > p2card:
        print('player one wins!!!')
        p1.extend(pile)
        pile.clear()

    elif p1card < p2card:
        print('player two wins!!!')
        p2.extend(pile)
        pile.clear()
    
    elif p1card == p2card:
        print('war')
        pile.append(p1.pop(0))
        pile.append(p2.pop(0))

if len(p2_deck) < 0:
    print('player two wins the game!!!!!!!!!!')
else:
    print('player one wins tho')