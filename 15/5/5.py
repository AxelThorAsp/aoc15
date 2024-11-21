#!/usr/bin/env python3
import sys

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

t = 0
for l in sys.stdin:
    line = l.strip()
    if ok(line):
        t+=1

print(t)
