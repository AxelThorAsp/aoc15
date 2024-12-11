#!/usr/bin/env python3
import sys
from math import log10
from functools import lru_cache

stones = [20, 82084, 1650, 3, 346355, 363, 7975858, 0]
@lru_cache(maxsize=None)
def transform(stone):
    if stone == 0:
        return (False, 1)
    if int(log10(stone)) % 2 == 1:
        s = str(stone)
        return (int(s[:len(s)//2]),int(s[len(s)//2:]))
    return (False, 2024 * stone)

curr = stones
for i in range(25):
    print(i)
    newl = []
    for s in curr:
        split, new = transform(s)
        if not split:
            newl.append(new)
        else:
            newl.append(split)
            newl.append(new)
    curr = newl

print(len(curr))
