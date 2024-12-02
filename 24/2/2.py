import sys
from functools import reduce

l = [list(map(int, line.split())) for line in sys.stdin]
def safe2(a,b):
    return abs(a-b) < 4 and abs(a-b) > 0
def safe(line):
    return all([line[i] < line[i+1] and safe2(line[i],line[i+1]) for i in range(len(line)-1)]) or all([line[i] > line[i+1] and safe2(line[i],line[i+1]) for i in range(len(line)-1)])

print([safe(line) for line in l].count(True))    


