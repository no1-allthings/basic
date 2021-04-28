bb = {1:'서', 2:'동' ,3:'북', 4:'남'}
cc={}
cc[10]='동서'


print(bb.values())
print(cc)
print(cc[10])
print(cc.keys())
del cc[10]
print(cc)

for i in bb.items():
    print(i)
    print(type(i))
for a,b in bb.items():
    print(a,b)
    print(type(b))