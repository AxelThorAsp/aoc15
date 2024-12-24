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

def nbors_all(p):
    x,y = p
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= dx+x < W and 0 <= y+dy < H:
            yield (x+dx,y+dy)

def cheat(p):
    x,y = p
    for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
        if 0 <= dx+x < W and 0 <= y+dy < H and M[y+dy][x+dx] != "#":
            yield (x+dx,y+dy)
@cache
def cheat2(start):
    end = set() 
    visited = set() 
    d = deque([(start, 0)])
    while d:
        curr, dist = d.popleft()
        x, y = curr
        if curr in visited or dist > 20:
            continue
        visited.add(curr)
        if M[y][x] == "#":
            for nbor in nbors_all(curr):
                if nbor not in visited:
                    d.append((nbor, dist + 1))
            continue
        for nbor in nbors_all(curr):
            if nbor not in visited:
                d.append((nbor, dist + 1))
        end.add((curr, dist))
    return end


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
lend = bfs(END)
cheats = set()
print(len(l))
for i, p in enumerate(l):
    print(i)
    for pp, w in cheat2(p):
        if l[p] + 100 >= l[END]:
            continue
        n = bfs(pp)[END]+l[p]+w
        if n < l[END] and (l[END] - n) >= 100:
            cheats.add((p,pp))
print(len(cheats))
