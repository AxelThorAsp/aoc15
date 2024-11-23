#!/usr/bin/env python3
import sys

d = dict()

for l in sys.stdin:
    nodes, w = l.split("=")
    n1, n2 = map(lambda x: x.strip(), nodes.split("to"))
    ww = int(w.strip())
    if n1 not in d:
        d[n1] = []
    d[n1].append((n2, ww))
    if n2 not in d:
        d[n2] = []
    d[n2].append((n1, ww))


def dfs(node, seen, l):
    global max_seen
    seen.add(node)
    if all(n[0] in seen for n in d[node]):
        max_seen = max(max_seen, l)
    else:
        for nbor, w in d[node]:
            if nbor not in seen:
                dfs(nbor, seen, l+w)
    seen.remove(node)

max_seen = 0
for k in d:
    dfs(k, set(), 0)
print(max_seen)
