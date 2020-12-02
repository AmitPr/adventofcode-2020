
with open("2.in") as f:
    lines = f.readlines()
valid = 0
valid2=0
for l in lines:
    minl = int(l.split('-')[0])
    maxl = int(l.split('-')[1].split(" ")[0])
    letter = l.split('-')[1].split(":")[0][-1]
    pw = l.split('-')[1].split(": ")[1].strip()
    if minl<=pw.count(letter)<=maxl:
        valid+=1
    if pw[minl-1]!=pw[maxl-1] and (pw[minl-1]==letter or pw[maxl-1]==letter):
        valid2+=1
print(valid,valid2)