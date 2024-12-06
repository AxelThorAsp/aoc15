#!/usr/bin/env python3
import sys
from collections import defaultdict
from copy import deepcopy

M = [list(l.strip()) for l in sys.stdin.readlines()]
#M = [list(l.strip()) for l in open("sample").readlines()]
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRS = [UP,RIGHT,DOWN,LEFT]

def get_start():
    for y, l in enumerate(M):
        for x, c in enumerate(l):
            if c == '^':
                start = (x,y)
                M[y][x] = '.'
                return start
START = get_start()

def get_next_step(pos, direction):
    xnew, ynew = pos[0] + direction[0], pos[1] + direction[1]
    return (xnew, ynew)

def turn(istep):
    return DIRS[(istep)% 4]

def can_step(m, pos, direction):
    xnew, ynew = get_next_step(pos, direction)
    return (xnew >= 0 and xnew < len(m[0])) and (ynew >= 0 and ynew < len(m))

def is_next_barrier(m, pos, direction):
    xnew, ynew = get_next_step(pos, direction)
    return m[ynew][xnew] == "#"

def step_or_turn(m, pos, direction):
    global numturn
    if not can_step(m, pos, direction):
        return (False, None)
    if is_next_barrier(m, pos, direction):
        numturn += 1
        return (pos, turn(numturn))
    new_pos = get_next_step(pos, direction)
    return (new_pos, direction)    

seen = set()
seen.add(START)
pos, dr = step_or_turn(M, START, UP)
seen.add(pos)
numturn = 0
while True:
    pos, dr = step_or_turn(M, pos, dr)
    if not pos:
        break
    seen.add(pos)
print(len(seen))

#p2
cycles = 0
for coord in seen:
    numturn = 0
    dirmap = defaultdict(set)
    if coord == START:
        continue
    cpy = deepcopy(M)
    x, y = coord
    cpy[y][x] = "#"
    dirmap[START].add(UP)
    pos, dr = step_or_turn(cpy, START, UP)
    dirmap[pos].add(dr)
    while True:
        pos, dr = step_or_turn(cpy, pos, dr)
        if not pos:
            break
        if dr in dirmap[pos]:
            cycles += 1
            break
        dirmap[pos].add(dr)
print(cycles)

