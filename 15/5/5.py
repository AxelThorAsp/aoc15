#!/usr/bin/env python3
import sys
from collections import defaultdict

vowels = {'a','e','i','o','u'}
banned = {'a' : 'b', 'c' : 'd', 'p' : 'q', 'x' : 'y'}

def ok(line):
    vcount = 0
    double = False
    for i, c in enumerate(line):
        if vcount < 3 and c in vowels:
            vcount += 1
        if i < (len(line) - 1):
            p = banned.get(c, "_")
            if p != '_' and line[i+1] == p:
                return False
            if line[i + 1] == c:
                double = True
    return double and vcount > 2


def ok2(line):
    d = defaultdict(int)
    between = False
    last_seen = {}
    for i, c in enumerate(line):
        if i < len(line) - 1:
            key = line[i:i+2]
            if key in d and last_seen[key] == i - 1:
                pass
            else:
                d[key] += 1
                last_seen[key] = i
        if i < len(line) - 2:
            if line[i] == line[i + 2]:
                between = True
    return between and len([_ for _ in d.values() if _ > 1])

t = 0
for l in sys.stdin:
    line = l.strip()
    if ok2(line):
        t+=1
print(t)
