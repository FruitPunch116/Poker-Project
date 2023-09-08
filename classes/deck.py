import random

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        
        value_name = ""
        suit_name = ""
        
        if self.value == 0:
            value_name = "Two"
            
        if self.value == 1:
            value_name = "Three"
            
        if self.value == 2:
            value_name = "Four"
            
        if self.value == 3:
            value_name = "Five"
            
        if self.value == 4:
            value_name = "Six"
            
        if self.value == 5:
            value_name = "Seven"
            
        if self.value == 6:
            value_name = "Eight"
            
        if self.value == 7:
            value_name = "Nine"
            
        if self.value == 8:
            value_name = "Ten"
            
        if self.value == 9:
            value_name = "Jack"
            
        if self.value == 10:
            value_name = "Queen"
            
        if self.value == 11:
            value_name = "King"
            
        if self.value == 12:
            value_name = "Ace"
            
        if self.suit == 0:
            suit_name = "Spade"
        
        if self.suit == 1:
            suit_name = "Diamond"
            
        if self.suit == 2:
            suit_name = "Club"
            
        if self.suit == 3:
            suit_name = "Heart"
            
        return value_name + " of " + suit_name

class StandardDeck(list):
    
    def __init__(self):
        super().__init__()
        suits = list(range(4))
        values = list(range(13))
        
        [[self.append(Card(value, suit)) for suit in suits] for value in values]
        
    def shuffle(self):
        random.shuffle(self)
        print("Deck is being shuffled")
        
    def deal(self, location):
        location.cards.append(self.pop(0))
        
deck = StandardDeck()