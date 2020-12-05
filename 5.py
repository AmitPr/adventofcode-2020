import numpy as np
import math
import collections

with open("5.in") as f:
    lines = [l.strip() for l in f.readlines()]

def find_row(st, max, min):
    mid = (max+min)//2
    if st[0]=='F' or st[0]=='L':
        if len(st[1:]):
            return find_row(st[1:],mid,min)
        else:
            return min
    else:
        if len(st[1:]):
            return find_row(st[1:],max,mid)
        else:
            return max-1
biggest = -1
ids = []
for i in lines:
    row = find_row(i[:7],128,0)
    col = find_row(i[7:],8,0)
    id = row*8 + col
    ids.append(id)
    if id> biggest:
        biggest = id
print(biggest)
for i in ids:
    for j in ids:
        if abs(i-j)==2 and not ((i+j)/2)in ids:
            print((i+j)//2)