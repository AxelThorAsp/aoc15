#!/usr/bin/env python3
import sys
import re
from functools import lru_cache

def tokenize(expr):
    pattern = r'\d+|->|AND|OR|LSHIFT|RSHIFT|NOT|\w+'
    return re.findall(pattern, expr)

d = {}

def parse(expr):
    if expr[0] == "NOT":
        return (~solve(expr[1]) & 0xFFFF)
    if (len(expr) == 1 and expr[0].isalpha()):
        return solve(expr[0])
    if expr[1] == "LSHIFT":
        return (solve(expr[0]) << solve(expr[2]) & 0xFFFF)
    if expr[1] == "RSHIFT":
        return (solve(expr[0]) >> solve(expr[2]) & 0xFFFF)
    if expr[1] == "AND":
        return (solve(expr[0]) & solve(expr[2]) & 0xFFFF)
    if expr[1] == "OR":
        return (solve(expr[0]) | solve(expr[2]) & 0xFFFF)
    assert False

@lru_cache(maxsize=2**16)
def solve(rhs):
    if rhs.isnumeric():
        return int(rhs)
    val = d[rhs]
    if len(val) == 1 and val[0].isnumeric():
        return int(val[0])
    return parse(val)


for l in sys.stdin:
    lhs, rhs = map(lambda x: x.strip(), l.split('->'))
    d[rhs] = tokenize(lhs)

target = 'a'
print(solve(target))