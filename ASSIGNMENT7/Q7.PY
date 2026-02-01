import random

cards = list(range(52))
random.shuffle(cards)
hand = cards[:5]

print("Total deck:", cards)
print("5 cards drawn:", hand)
