#!/usr/bin/env python3
import sys
from collections import defaultdict

r, l = sys.stdin.read().split("\n\n")

d = defaultdict(set)

def do(l):
    for i, c in enumerate(l):
        if not set(l[i+1:]) <= d[c]:
            return False
    return True

for rr in r.split("\n"):
    k,v = map(int, rr.split("|"))
    d[k].add(v)
c = 0
for ll in l.strip().split("\n"):
    ls = list(map(int, ll.split(",")))
    if do(ls):
        c+=ls[len(ls)//2]

print(c)
