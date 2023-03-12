import numpy as np
from random import randint
from sim_classes import *


x = Player(10)


for _ in range(10):
    h = Hand()
    for i in range(10):
        h.add_card(Card(randint(1,13)))
        print(h.value, h.soft, str(h))

s = CountedShoe(8)
for _ in range(400):
    print(str(s.draw()),s.penetration,s.count,s.true)
print(str(s))
