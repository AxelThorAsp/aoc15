#!/usr/bin/env python3
import sys
from collections import defaultdict

lines = [list(line.strip()) for line in sys.stdin.readlines()]

antennas = defaultdict(list)
antinodes = set()

for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c != '.':
            antennas[c].append((x,y))

def slope(a, b):
    x1, y1 = a
    x2, y2, = b
    return (x2-x1),(y2-y1)

for antenna in antennas:
    for a in antennas[antenna]:
        for b in antennas[antenna]:
            if a == b:
                continue
            dx, dy = slope(a,b)
            antix, antiy = (a[0]-dx, a[1]-dy)
            if antiy >= 0 and antiy < len(lines) and antix >= 0 and antix < len(lines[0]):
                lines[antiy][antix] = '#'
                antinodes.add((antix,antiy))
print(len(antinodes))
