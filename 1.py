with open("1.in","r+") as f:
    arr = [int(x) for x in f.readlines()]
for i in arr:
    for j in arr:
        if i+j==2020:
            print(i*j,i,j)
            break

for i in arr:
    for j in arr:
        for k in arr:
            if i+j+k==2020:
                print(i*j*k,i,j,k)
                break