a={}
a[1]='a'
a['g']=3
a[4]=4
a['h']='h'
print(a)
print(len(a))
del a[4]
print('h' in a)
print(a.items())

print(tuple(a))
d3 = ((1,2),(2,3),(3,5))
d4 = ('ab','23','4c')
d5=(12,34,56)

print(dict(d3))
print(dict(d4))
print(dict(d5))



