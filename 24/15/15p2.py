#!/usr/bin/env python3
import sys
S = sys.stdin.read()
S = S.replace("#", "##")
S = S.replace("O", "[]")
S = S.replace(".", "..")
S = S.replace("@", "@.")

M, D = map(lambda x: x.strip(), S.split("\n\n"))
D = "".join(D.split('\n'))
M = [l for l in M.split('\n')]
M = [list(l.strip()) for l in M]
WALL = "#"
BOX = "[]"
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

get_start()
def step(pos, d):
    x, y=pos
    dx, dy = d
    return M[y+dy][x+dx]


def get_boxes(pos, d):
    i = 0
    curr = [pos]
    while i < len(curr):
        cp = curr[i]
        if step(cp,d) == "#":
            return None
        if step(cp,d) in "[]" and (cp[0]+d[0],cp[1]+d[1]) not in curr:
            curr.append((cp[0]+d[0],cp[1]+d[1]))
        if M[cp[1]][cp[0]] == "[" and (cp[0]+1,cp[1]) not in curr:
            curr.append((cp[0]+1,cp[1]))
        if M[cp[1]][cp[0]] == "]" and (cp[0]-1,cp[1]) not in curr:
            curr.append((cp[0]-1,cp[1]))
        if M[cp[1]][cp[0]] == "#":
            return None
        i+=1
    return curr

def show(s):
    for i in range(len(M)):
        for ii in range(len(M[0])):
            if (ii,i) == pos:
                print(s,end="")
            else:
                print(M[i][ii],end="")
        print()

pos = START
for s in D:
    dd = DMAP[s]
    dx, dy = dd
    cx, cy = pos
    next_block = M[cy+dy][cx+dx]
    if next_block == WALL:
        continue
    elif next_block == '[' or next_block == ']':
        # found box
        all_boxes = get_boxes((cx+dx,cy+dy), dd)
        if all_boxes is not None:
            # make copy
            dic = {(x,y):M[y][x] for x,y in all_boxes}
            for x,y in all_boxes:
                M[y][x] = '.'
            for x,y in all_boxes:
                M[y+dy][x+dx] = dic[(x,y)]
            pos = (cx+dx, cy+dy)
    else:
        pos = (cx+dx, cy+dy)
p = 0
for y, l in enumerate(M):
    for x, c in enumerate(l):
        if c == '[':
            p+=100*y+x
print(p)
