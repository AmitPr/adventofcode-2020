import numpy as np
import math
import collections

h = "#0123456789abcdef"

with open("4.in") as f:
    lines = [l.strip() for l in f.readlines()]
i=0
v1 = 0
v2 = 0
while i<len(lines):
    x= lines[i]
    x=x.replace(' ',':').split(":")
    present = dict(zip(x[::2] ,x[1::2]))
    i+=1
    while i<len(lines) and len(lines[i]) :
        x= lines[i].replace(' ',':').split(":")
        present.update(dict(zip(x[::2] ,x[1::2])))
        i+=1
    i+=1
    if {"byr","iyr","eyr","hgt","hcl","ecl","pid"}.issubset(present):
        #print(present)
        cur = True
        v1+=1
        if not 1920<=int(present["byr"])<=2002:
            cur = False
        if not 2010<=int(present["iyr"])<=2020:
            cur = False
        if not 2020<=int(present["eyr"])<=2030:
            cur = False
        if "cm" in present["hgt"]:
            if not 150<=int(present["hgt"].split("cm")[0])<=193:
                cur = False
        elif "in" in present["hgt"]:
            if not 59<=int(present["hgt"].split("in")[0])<=76:
                cur = False
        else:
            cur=False
        if not (len(present["hcl"])==7 and all(c in h for c in present["hcl"]) and present["hcl"][0]=='#'):
            cur = False
        if not (present["pid"].isnumeric() and len(present["pid"])==9):
            cur = False
        if not (present["ecl"] in ['amb', 'blu' ,'brn' ,'gry' ,'grn' ,'hzl' ,'oth']):
            cur = False
        if cur:
            v2+=1
print(v1,v2)