#!/usr/bin/env python3
import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)

@lru_cache(maxsize=10**6)
def do(inp):
    if all(ord(x) == ord(inp[0]) for x in inp):
        return len(inp) + 1
    if len(inp) == 1:
        return 2
    first = inp[0]
    for i, c in enumerate(inp):
        if c != first:
            return do(inp[:i]) + do(inp[i:])

s = "3113322113"
for i in range(40):
    print(do.cache_info())
    s = do(s)
    print(s)
