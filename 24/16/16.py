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

def nbors(pos):
    x,y = pos
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if M[y+dy][x+dx] != "#":
            yield ((x+dx, y+dy),(dx,dy))

def dijkstra(start, end):
    heap = [(0, start)]
    dist = {start: 0}  
    dirr = {start: (1,0)}
    while heap:
        curr_dist, node = heapq.heappop(heap)
        if node == end:
            return curr_dist
        for nbor, d in nbors(node):
            delta = 1001 if dirr[node] != d else 1
            new_dist = curr_dist + delta
            if nbor not in dist or new_dist < dist[nbor]:
                dist[nbor] = new_dist
                dirr[nbor] = d
                heapq.heappush(heap, (new_dist, nbor))
    return -1

print(dijkstra(START, END))
