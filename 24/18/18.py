from collections import deque
import sys

S = sys.stdin.read().strip()

coordsl = list(tuple(map(int,c.split(","))) for c in S.splitlines())
take = 1024
coords = set(coordsl[:take])
H = 71
W = 71
M = [['.' for _ in range(W)] for _ in range(H)]
for y in range(H):
    for x in range(W):
        if (x,y) in coords:
            M[y][x] = "#"

def show():
    for y, l in enumerate(M):
        for x, c in enumerate(M[y]):
            print(c,end="")
        print()


for y in range(H):
    for x in range(W):
        if (x,y) in coords:
            M[y][x] = "#"

for i in range(5000):
    def nbors(p):
        x,y = p
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx = x+dx; ny=y+dy
            if 0 <= nx < W and 0 <= ny < H and M[ny][nx] != "#":
                yield (nx,ny)
    def do(i):
        take = 1024 + i
        coords = set(coordsl[:take])
        for y in range(H):
            for x in range(W):
                if (x,y) in coords:
                    M[y][x] = "#"
        dist = {(0,0): 0}
        dq = deque([(0,0)])
        def bfs(d: deque):
            while d:
                curr = d.popleft()
                for nbor in nbors(curr):
                    if nbor not in dist:
                        dist[nbor] = dist[curr]+1
                        d.append(nbor)
        bfs(dq)
        print(i)
        print(coordsl[i+1023])
        print(dist[(70,70)])
    do(i)
show()


