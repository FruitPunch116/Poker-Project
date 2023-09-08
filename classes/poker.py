from deck import deck
from player import player1

deck.shuffle()
print(deck)

deck.deal(player1)

print(f"{player1.name} has {player1.cards}")