#!/usr/bin/env python3
import sys
import re
import numpy as np

BIG = 10000000000000
D = sys.stdin.read()

P = D.split("\n\n")

def nums(l):
    return map(int,re.findall(r"\d+",l))

def close_enough(n):
    return abs(n - np.round(n)) < 0.001

def solve(A,b):
    try:
        return np.linalg.solve(A,b)
    except LinAlgError:
        print(":(")
t = 0
for p in P:
    p=p.strip()
    a, b, pz = p.split('\n')
    a1,a2 = nums(a)
    b1,b2 = nums(b)
    p1,p2 = nums(pz)
    p1 += BIG
    p2 += BIG
    x = solve([[a1,b1],[a2,b2]],[p1,p2])
    if all(close_enough(n) for n in x):
        t+= 3*x[0] + x[1]
print(t)



