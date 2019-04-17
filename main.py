from random import shuffle

WIDTH = 1024
HEIGHT = 768

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
        
    def value(self):
        # return a tuple of values to handle the Ace
        face = ['J','Q','K']
        if self.rank in face:
            return (10,10)
        elif self.rank=='A':
            return (1,11)
        else:
            return (int(self.rank),int(self.rank))
        
class Deck:
    def __init__(self):
        self.cards = []
        ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suits = ['Club','Diamonds','Hearts','Spades']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))
        shuffle(self.cards)
    

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = [self.deck.cards.pop(),self.deck.cards.pop()]
        self.dealer = [self.deck.cards.pop(),self.deck.cards.pop()]
        
    
    def check_hands(self):
        player_score = [0,0]
        for card in self.player:
            pass
            # need to check player score
            
        
        # check dealer score
        
        

        