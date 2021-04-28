f=[1,3,5,2,1,3,4,5,2,7,6,4,3,5]

d={}

for f in f:
    if f in d:
        d[f] += 1
    else:
        d[f]=1

print(d)
