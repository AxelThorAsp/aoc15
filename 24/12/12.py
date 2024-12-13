#!/usr/bin/env python3
import sys

D = [list(l.strip()) for l in sys.stdin.readlines()]

H = len(D)
W = len(D[0])
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_bounds(x,y):
    return 0 <= x < W and 0 <= y < H

def nbors(x, y):
    # All positions
    for dx, dy in DIRS:
            yield (x+dx, y+dy)

class Ref:
    def __init__(self):
        self.fence = 0
        self.sides = []
        self.side_c = 0

def walk(x, y, seen, fences):
    seen.add((x,y))
    for nbor in nbors(x,y):
        xn, yn = nbor
        if not in_bounds(xn, yn) or D[yn][xn] != D[y][x]:
            # not in bounds or not same plant
            # therefore, fence here
            fences.fence+=1
            fences.sides.append(((x,y),(xn,yn)))
            continue
        if nbor not in seen:
            walk(xn, yn, seen, fences)
    return seen
def do(l):
    s = set()
    for p1,p2 in l:
        ok = True
        x,y = p1
        x1,y1 = p2
        for dx,dy in [(1,0),(0,1)]:
            if ((x+dx,y+dy),(x1+dx,y1+dy))in l:
                ok = False
        if ok:
            s.add((p1,p2))
    return len(s)

area = 0
p2 = 0
GLOBAL_SEEN = set()
for y, l in enumerate(D):
    for x, p in enumerate(D[y]):
        if (x,y) in GLOBAL_SEEN:
            continue
        ref = Ref()
        s = walk(x,y,set(), ref)
        p2+=len(s)*do(set(ref.sides))
        GLOBAL_SEEN.update(s)
        area+=len(s) * ref.fence
print(area)
print(p2)
