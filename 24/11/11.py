#!/usr/bin/env python3
import sys
from math import log10
from functools import lru_cache

stones = [20, 82084, 1650, 3, 346355, 363, 7975858, 0]

@lru_cache(maxsize=None)
def transform(stone, depth):
    if depth == 0:
        return 0
    if stone == 0:
        return transform(1,depth-1)
    if int(log10(stone)) % 2 == 1:
        s = str(stone)
        return 1 + transform(int(s[:len(s)//2]),depth-1) + transform(int(s[len(s)//2:]), depth-1)
    return transform(2024 * stone, depth-1)

p2 = 0
p1 = 0
for s in stones:
    p2+=transform(s,75)
    p1+=transform(s,25)
print(p1+len(stones))
print(p2+len(stones))
