#!/usr/bin/env python3
from itertools import islice
import sys
short = list(map(int, "12345"))
sample = list(map(int, "2333133121414131402"))
big = sys.stdin.read().strip()
big = list(map(int,big))


def get_block(inp):
    blocks = []
    filenum = 0
    for i, c in enumerate(inp):
        if i % 2:
            blocks.extend('.'*c)
        else:
            blocks.extend([filenum]*c)
            filenum+=1
    return blocks
def get_filenum(b):
     return sum(1 for i in b if i != '.')

blocks = get_block(big)
numfiles = get_filenum(blocks)

SPACES = [i for i in range(len(blocks)) if blocks[i] == '.']
spaces_iter = iter(SPACES)

def get_next(my_list):
        for i in range(len(my_list) - 1, -1, -1):
             if my_list[i] == '.':
                  continue
             else:
                  yield my_list[i]
          
ret = [elem for elem in blocks]
zz = zip(get_next(blocks), spaces_iter)
for elem, i in islice(zz, numfiles):
     ret[i] = elem
print(sum(i*c for i,c in enumerate(ret[:numfiles])))