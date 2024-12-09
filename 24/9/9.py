#!/usr/bin/env python3
from itertools import islice
import sys
big = sys.stdin.read().strip()
big = list(map(int,big))

class Block:
     def __init__(self, size, _id, index):
          self.size = size
          self._id = _id
          self.index = index

     def __repr__(self):
        return f"{str(self._id)*self.size}"

class Span:
     def __init__(self, size, index):
          self.size = size
          self.index = index

     def __repr__(self):
        return f"index: {self.index}, size: {self.size}"

def show(b):
     print("".join(map(str,b)))

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

def get_next(my_list):
        for i in range(len(my_list) - 1, -1, -1):
             if my_list[i] == '.':
                  continue
             yield my_list[i]

def part1():  
    ret = [elem for elem in blocks]
    zz = zip(get_next(blocks), iter(SPACES))
    for elem, i in islice(zz, numfiles):
        ret[i] = elem
    print(sum(i*c for i,c in enumerate(ret[:numfiles])))
part1()

# p2
def get_block_2(inp):
    blocks = []
    spans = []
    filenum = 0
    index = 0
    for i, c in enumerate(inp):
        if not i % 2:
            blocks.append(Block(int(c), filenum, index))
            filenum+=1
        else:
            spans.append(Span(int(c), index))
        index+=c

    return blocks, spans

blocks2, spans = get_block_2(big)
retp2 = [elem for elem in blocks]
spans_idx = 0

def canput(b):
     for span in spans:
          assert span.size >= 0
          if span.size > 0 and span.size >= b.size and span.index < b.index:
               return span
     return None

def put(b, span):
     assert span.index < b.index
     assert b.size >= 0
     for i in range(b.size):
          retp2[i + span.index] = b._id
     span.size = span.size - b.size
     span.index = span.index + b.size
     for i in range(b.size):
          retp2[b.index + i] = '.'

for b in reversed(blocks2):
     span = canput(b)
     if span:
          put(b, span)
t2 = 0
for i, c in enumerate(retp2):
    if c == '.':
         continue
    t2+=i*c
print(t2)
