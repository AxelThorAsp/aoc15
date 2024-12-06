#!/usr/bin/env python3
import sys

M = [list(l.strip()) for l in sys.stdin.readlines()]

start = (0,0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIR = UP
for y, l in enumerate(M):
    for x, c in enumerate(l):
        if c == '^':
            start = (x,y)
            M[y][x] = '.'

seen = set()
DIRS = [UP,RIGHT,DOWN,LEFT]
it = 1
pos = start
while True:
    if pos[0] < 0 or pos[0] >= len(M[0]):
        break
    if pos[1] < 0 or pos[1] >= len(M):
        break
    curx, cury = pos
    seen.add((curx,cury))
    dx, dy = DIR
    newx, newy = (curx+dx, cury+dy)
    try:
        if M[newy][newx] == '#':
            DIR = DIRS[it % 4]
            it += 1
            dx, dy = DIR
            newx, newy = (curx+dx, cury+dy)
            pos = (newx, newy)
        else:
            pos = (newx, newy)
    except IndexError:
        break

print(len(seen))


