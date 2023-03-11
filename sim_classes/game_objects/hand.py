import numpy as np
from .card import Card

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
