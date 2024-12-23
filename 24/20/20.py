from collections import deque
from functools import cache
import sys

S = sys.stdin.read().strip()

M = [list(l) for l in S.splitlines()]
W = len(M[0])
H = len(M)
START = (-1,-1)
END = (-1,-1)

for y, l in enumerate(M):
    for x, c in enumerate(M[y]):
        if c == "S":
            START = (x,y)
        elif c == "E":
            END = (x,y)

def nbors(p):
    x,y = p
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= dx+x < W and 0 <= y+dy < H and M[y+dy][x+dx] != "#":
            yield (x+dx,y+dy)

def cheat(p):
    x,y = p
    for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
        if 0 <= dx+x < W and 0 <= y+dy < H and M[y+dy][x+dx] != "#":
            yield (x+dx,y+dy)
@cache
def bfs(s):
    d = deque([(s)])
    distto = {s : 0}
    while d:
        curr = d.popleft()
        for nbor in nbors(curr):
            if nbor not in distto:
                distto[nbor] = distto[curr] + 1
                d.append(nbor)
    return distto

l = bfs(START)
cheats = set()
print(len(l))
for i, p in enumerate(l):
    for pp in cheat(p):
        if pp in l and l[pp] >= l[END] - 100:
            continue
        n = bfs(pp)[END]+l[p]+2
        if n < l[END] and (l[END] - n) >= 100:
            cheats.add((p,pp))
print(len(cheats))
