#!/usr/bin/env python3
import sys

M = [list(l.strip()) for l in sys.stdin.readlines()]
H = len(M)
W = len(M[0])

class Point:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.nbors = []
    def __repr__(self):
        return f"x={self.x}, y={self.y}, val={self.val}"

def get_points():
    points = []
    for y, r in enumerate(M):
        for x, c in enumerate(r):
            val = int(c)
            points.append(Point(x, y, val))
    return points

POINTS = get_points() 

def get_point(x,y):
    return POINTS[W*y+x]

def nbors(point):
    x = point.x
    y = point.y
    points=[]
    dirs = [(-1,0),(1,0),(0,1),(0,-1)]
    for dx, dy in dirs:
        if 0 <= x + dx < W and 0 <= y + dy < H:
            points.append(get_point(x+dx,y+dy))
    return points
            
def cango(ffrom, to):
    return ffrom.val == to.val - 1


class DFS:
    def __init__(self):
        self.seen = 0

    def search(self, p):
        def dfs(p, l, seen_set):
            seen_set.add((p.x,p.y))
            if p.val == 9:
                self.seen+=1
            for nbor in nbors(p):
                if cango(p, nbor) and (nbor.x, nbor.y) not in seen_set:
                    dfs(nbor, l+1, seen_set)
        dfs(p, 0, set())
        return self

    def search2(self, p):
        def dfs(p, l, seen_set):
            seen_set.add((p.x,p.y))
            if p.val == 9:
                self.seen+=1
            for nbor in nbors(p):
                if cango(p, nbor) and (nbor.x, nbor.y) not in seen_set:
                    dfs(nbor, l+1, seen_set)
            seen_set.remove((p.x,p.y))
        dfs(p, 0, set())
        return self
# p1
t = 0
for p in POINTS:
    if p.val == 0:
        t+= DFS().search(p).seen
print("p1\n",t)

# p2
t = 0
for p in POINTS:
    if p.val == 0:
        t+= DFS().search2(p).seen
print("p2\n",t)