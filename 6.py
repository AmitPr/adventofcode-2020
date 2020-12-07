import numpy as np
import math
import collections

inp = []
with open("6.in") as f:
    lines = f.readlines()
    i=0
    while i < len(lines):
        group = []
        while lines[i].strip():
            group.append(lines[i].strip())
            i+=1
        i+=1
        inp.append(group)
yes = 0
y2=0
for group in inp:
    x = set(''.join(group))
    for i in x:
        in_all = True
        for j in group:
            if not i in j:
                in_all=False
        if in_all:
            y2+=1
    score = len(x)
    yes+=score
print(yes)
print(y2)