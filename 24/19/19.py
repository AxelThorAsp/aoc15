#!/usr/bin/env python3
from functools import cache
import sys

S = sys.stdin.read().strip()

O, L = S.split("\n\n")
options = O.replace(" ", "").split(",")
lines = L.splitlines()

@cache
def solve(w: str) ->int:
    if w == "":
        return 1
    c = 0
    for op in options:
        if w.startswith(op):
            c += solve(w[len(op):])
    return c

p1 = 0
p2 = 0
for l in lines:
    r = solve(l)
    if r > 0:
        p1 += 1
    p2 += r

print(p1)
print(p2)
