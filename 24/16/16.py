import heapq
import sys
S = sys.stdin.read()
M = [list(l) for l in S.strip().split('\n')]
START = (-1,-1)
END = (-1,-1)
for y, l in enumerate(M):
    for x, c in enumerate(M[y]):
        if c == 'S':
            START = (x,y)
        if c == 'E':
            END = (x,y)
# left down right up
DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
def nbors(pos, d):
    x,y = pos
    dx,dy = DIRS[(d)]
    if M[y+dy][x+dx] != "#":
        yield (1,(x+dx,y+dy),d)
    yield (1000,(x, y),(d+1)%4)
    yield (1000,(x, y),(d+3)%4)

def dijkstra(start, end):
    heap = [(0, (start, 2))]
    dist = {(start, 2): 0}  
    pred = {(start, 2): []}
    while heap:
        curr_dist, _node = heapq.heappop(heap)
        node, dn = _node
        for w, nbor, dd in nbors(node, dn):
            new_dist = w + curr_dist
            if (nbor,dd) not in dist:
                dist[(nbor,dd)] = 9999999999999999999
                pred[(nbor,dd)] = []
            if new_dist < dist[(nbor,dd)]:
                dist[(nbor,dd)] = new_dist
                pred[(nbor,dd)] = [(node, dn)]
                heapq.heappush(heap, (new_dist, (nbor, dd)))
            elif new_dist == dist[(nbor,dd)]:
                pred[(nbor,dd)].append((node,dn))

    return dist, pred
p1, pred = dijkstra(START, END)

seen = set()
def do(pair):
    p,d = pair
    seen.add(p)
    for k in pred[pair]:
        do(k)

do((END,3))
print(len(seen))
