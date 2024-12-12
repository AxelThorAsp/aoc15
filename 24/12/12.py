#!/usr/bin/env python3
import sys

D = [list(l.strip()) for l in sys.stdin.readlines()]

H = len(D)
W = len(D[0])
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

"""
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

def in_bounds(x,y):
    return 0 <= x < W and 0 <= y < H

def nbors(x, y):
    # All positions
    for dx, dy in DIRS:
            yield (x+dx, y+dy)

class Ref:
    def __init__(self):
        self.fence = 0

def walk(x, y, seen, fences):
    seen.add((x,y))
    for nbor in nbors(x,y):
        xn, yn = nbor
        # not in bounds or not same plane
        # therefore, fence here
        if not in_bounds(xn, yn) or D[yn][xn] != D[y][x]:
            # maybe add check for in seen ?
            fences.fence+=1
            continue
        if nbor not in seen:
            walk(xn, yn, seen, fences)
    return seen

area = 0
GLOBAL_SEEN = set()
for y, l in enumerate(D):
    for x, p in enumerate(D[y]):
        if (x,y) in GLOBAL_SEEN:
            continue
        ref = Ref()
        s = walk(x,y,set(), ref)
        print(ref.fence)
        GLOBAL_SEEN.update(s)
        area+=len(s) * ref.fence
        print(len(s))
print(area)
