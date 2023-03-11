import numpy as np

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

