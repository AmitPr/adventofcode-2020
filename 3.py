import numpy as np
import math
import collections

with open("3.in") as f:
    lines = [l.strip() for l in f.readlines()]

def nt(dx,dy):
    x,y=(0,0)
    trees=0
    while y<len(lines):
        if lines[y][x]=='#':
            trees+=1
        y+=dy
        x+=dx
        if x>=len(lines[0]):
            x-=len(lines[0])
    return trees
print(nt(3,1)*nt(1,1)*nt(5,1)*nt(7,1)*nt(1,2))