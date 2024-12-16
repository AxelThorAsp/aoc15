#!/usr/bin/env python3
import sys
S = sys.stdin.read()
#S = """ ########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

M, D = map(lambda x: x.strip(), S.split("\n\n"))
D = "".join(D.split('\n'))
M = [l for l in M.split('\n')]
M = [list(l.strip()) for l in M]
WALL = "#"
BOX = "O"
START = (-999, -999)
BOXES = []

DMAP = {
    '^' : (0, -1),
    'v' : (0, 1),
    '>' : (1, 0),
    '<' : (-1, 0)
}

def get_start():
    global START
    for y, l in enumerate(M):
        for x, c in enumerate(l):
            if c == '@':
                START = (x, y)
                M[y][x] = '.'
get_start()

def step(pos, d):
    x, y=pos
    dx, dy = d
    return M[y+dy][x+dx]

# does not include start
def all_in_range(start, stop, d):
    r = []
    while start != stop:
        n = (start[0]+d[0],start[1]+d[1])
        r.append(n)
        start = n
    return r

def get_next_wall(pos, d):
    dx, dy = d
    x, y = pos
    while step(pos, d) != WALL:
        x, y = pos
        pos = (x+dx,y+dy)
    return (pos[0]+dx,pos[1]+dy)

pos = START
for s in D:
    dd = DMAP[s]
    dx, dy = dd
    cx, cy = pos
    next_block = M[cy+dy][cx+dx]
    if next_block == WALL:
        continue
    elif next_block == BOX:
        between = all_in_range(pos, get_next_wall(pos, dd), dd)[:-1]
        if all(M[x[1]][x[0]] == BOX for x in between):
            pass
            #do nothing
        else:
            # find first empy spot
            first_empy = [p for p in between if M[p[1]][p[0]] == '.'][0]
            need_move = all_in_range(pos, first_empy, dd)[:-1]
            for x,y in need_move:
                M[y+dy][x+dx] = BOX
            pos = (cx+dx, cy+dy)
            M[cy+dy][cx+dx] = '.'
    else:
        pos = (cx+dx, cy+dy)
p = 0
for y, l in enumerate(M):
    for x, c in enumerate(l):
        if c == BOX:
            p+=100*y+x

print(p)
