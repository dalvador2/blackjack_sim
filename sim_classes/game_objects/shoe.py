import numpy as np
from random import randint
from .card import Card

class Shoe:
    def __init__(self,decks) -> None:
        self.decks = decks
        self.cards = np.array([Card(i) for i in range(1,14)]*decks*4,dtype=Card)
    
    def __str__(self) -> str:
        cards = [str(card) for card in self.cards]
        ret_str = ""
        for item in cards:
            ret_str += f"| {item} |"
        return ret_str
        
    def draw(self):
        if len(self.cards) == 0:
            raise IndexError("no more cards to deal in shoe")
        random_index = np.random.randint(0, len(self.cards))
        card = self.cards[random_index]
        self.cards = np.delete(self.cards,random_index)
        return card
    
    @property
    def penetration(self):
        return 1-(len(self.cards)/self.decks/13/4)

class CountedShoe(Shoe):
    def __init__(self, decks) -> None:
        self.count = 0
        super().__init__(decks)
    
    def draw(self):
        card = super().draw()
        self.update_count(card)
        return card
    
    def update_count(self,card):
        if 2<=card.card<=6:
            self.count+=1
        elif 10<=card.card<=13 or card.card == 1:
            self.count -=1
    
    @property
    def true(self):
        return self.count/(len(self.cards)/13/4)