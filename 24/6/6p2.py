#!/usr/bin/env python3
import sys
from copy import deepcopy
from collections import defaultdict

M = [list(l.strip()) for l in sys.stdin.readlines()]

start = (0,0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
for y, l in enumerate(M):
    for x, c in enumerate(l):
        if c == '^':
            start = (x,y)
            M[y][x] = '.'
def do(mm):
    DIR = UP
    global seen
    DIRS = [UP,RIGHT,DOWN,LEFT]
    it = 1
    pos = start
    while True:
        if pos[0] < 0 or pos[0] >= len(mm[0]):
            break
        if pos[1] < 0 or pos[1] >= len(mm):
            break
        curx, cury = pos
        if DIR in seen[pos]:
            return True
        seen[(curx,cury)].add((DIR[0], DIR[1]))
        dx, dy = DIR
        newx, newy = (curx+dx, cury+dy)
        try:
            if mm[newy][newx] == '#':
                DIR = DIRS[it % 4]
                it += 1
                dx, dy = DIR
                newx, newy = (curx+dx, cury+dy)
                pos = (newx, newy)
            else:
                pos = (newx, newy)
        except IndexError:
            break
    return False
seen = defaultdict(set)
do(M)
c=0
for p in seen:
    seen = defaultdict(set)
    cpy = deepcopy(M)
    x,y = p
    cpy[y][x] = "#"
    if p == start:
        print("found start")
        continue
    if do(cpy):
        c+=1
print(c)
