#! /usr/bin/env python3
import sys

m = [[0 for _ in range(1000)] for _ in range(1000)]

def solve(ins, x1, y1, x2, y2):
    action = 1 if ins == "on" else 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            m[j][i] = action

def toggle(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            m[j][i] = ~m[j][i] & 1

for l in sys.stdin:
    words = l.strip().split()
    if (words[0] == "toggle"): 
        x1, y1 = map(int, words[1].split(","))
        x2, y2 = map(int, words[3].split(","))
        toggle(x1, y1, x2, y2)
        continue
    ins = words[1]
    x1, y1 = map(int, words[2].split(","))
    x2, y2 = map(int, words[4].split(","))
    solve(ins, x1, y1, x2, y2)

print(sum([sum(m[i]) for i in range(1000)]))