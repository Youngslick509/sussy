import random


def evaluate(p1card, p2card, p1_deck, p2_deck, game_pile):
   
   
   
    import random

deck = list(range(2, 15)) * 4
random.shuffle(deck)
p1 = deck[:26]
p2 = deck[26:]
pile = []

while len(p1) != 0 or len(p2) != 0:

    p1 == deck.pop()
    p2 == p2.pop()

    if p1 == deck.pop(0):
        p2card = p2.pop[0]
        pile.apppend = (p1)
        pile.apppend = (p2card)

    print('player one has: ' + str(p1) + '\nplayer two has: ' + str(p2))

    if p1 > p2:
        print('player one wins!!!')
        p1.extend(pile)
        pile.clear()

    elif p1 < p2:
        print('player two wins!!!')
        p2.extend(pile)
        pile.clear()
    
    elif p1 == p2:
        print('war')
        pile.append(p1.pop(0))
        pile.append(p2.pop(0))

if len(p2) < 0:
    print('player two wins the game!!!!!!!!!!')
else:
    print('player one wins tho')