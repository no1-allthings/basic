# a=4
# b='4'
# c=4
# print(a+int(b))
# print(str(a)+b)
#
# if a>10:
#     print('hi')
# elif c<4:
#     print('bye')
# else:
#     print('false')

#리스트

# a = [1,2,3,4,]
# b = ['a','b',]
# c = [5,6,'c','c',]

# print(a+b)
# a[0]=7
# print(a)
# print(a[0])
# print(len(a))
# print(sorted(a))
# print(sum(a))
# print(a.index(7))
# print('a' in b)
# if 'c' in c:
#     print('yo')

#튜플
# d= (7,1,2,3,4,)
# e = ('a','b',)
# f = (5,6,'c','e',)
# print(d+e)
# # d[0]=7
# # print(d)
# print(d[0])
# print(len(f))
# print(sorted(d))
# print(sum(d))
# print(d.index(7))
# print('a' in e)
# if 'c' in e:
#     print('yo')
# else:
#     print('없다')

#dictionry
h= {1:11,2:22,3:33,4:44,}
i = {0:'a', 'age':5,'name':'aa',}

print(i)
h[0]=7
print(h)
print(i[0])
print(len(h))
print(sorted(h))
print(sum(h.values()))
#print(h.index(7))
print('a' in i)
if 'c' in i:
    print('yo')
else:
    print('없다')
print(i[0])
print(i.values())
print(i.keys())
print(i.items())
print(5 in i.values())

for key in i:
    print(key)
    print(i[key])

h[1]=111
print(h)
del h[1]
print(h)