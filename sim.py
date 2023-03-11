import numpy as np
from random import randint



class Card:
    def __init__(self,card) -> None:
        if not(1<=card<=13):
            raise ValueError("Value of card not between 1 and 13")
        if int(card) != card:
            raise ValueError("Card is not an integer value")
        self.card = card
    
    @property
    def value(self) -> int:
        if self.card == 1:
            return 11
        elif self.card >= 10:
            return 10
        else:
            return self.card
    
    @property
    def lowval(self) -> int:
        if self.card == 1:
            return 1
        elif self.card >= 10:
            return 10
        else:
            return self.card
    
    @property
    def ace(self) -> bool:
        return self.card == 1
    
    def __str__(self) -> str:
        card_dict = dict(zip(range(1,14),["A"]+[str(i) for i in range(2,11)]+["J","Q","K"]))
        return card_dict[self.card]
class Hand:
    def __init__(self) -> None:
        self.cards = np.empty(0,dtype=Card)
        self.aces = 0
        self.nerf = 0
    
    def __str__(self) -> str:
        cards = [str(card) for card in self.cards]
        ret_str = ""
        for item in cards:
            ret_str += f"| {item} |"
        return ret_str
    def add_card(self,card:Card):
        self.cards = np.append(card,self.cards)
        self.aces += card.ace
    
    @property
    def total(self) -> int:
        total = 0
        for item in self.cards:
            total += item.value
        return total-self.nerf
    
    @property
    def value(self) -> int:
        while self.soft and self.total > 21:
            self.nerf += 10
        return self.total
    
    @property
    def soft(self) -> bool:
        return self.aces > self.nerf//10

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



    

for _ in range(10):
    h = Hand()
    for i in range(10):
        h.add_card(Card(randint(1,13)))
        print(h.value, h.soft, str(h))

s = Shoe(8)
for _ in range(400):
    print(str(s.draw()),s.penetration)
print(str(s))