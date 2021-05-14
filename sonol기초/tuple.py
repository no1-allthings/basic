t1=()
t2=tuple()

t3=(1,'a',3,'b')
print(len(t3))
print(t3[0])
print('a' in t3)
print(t3.index(1))
print(t3.count('b'))
a,b,c ,d  = t3
print((d))


h= 10
k= 100
k,h = h,k
print(h,k)