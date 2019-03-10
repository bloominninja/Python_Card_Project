import cardEngine, operator
from random import shuffle

deck= cardEngine.Deck(True)
deck2=cardEngine.Deck(False)
shuffle(deck.Cards)
#deck.Cards.sort(key=operator.attrgetter('rank'))
#deck.Cards.sort(key=operator.attrgetter('suit'))
for y in range(51):
    deck.Draw().printcard()

card = deck.Draw()
print()
card.printcard()
print()
deck2.Place(card)
card = deck.Peek()
card.SetVisable(True)
card.printcard()
card = deck.Draw()
card = deck.Draw()