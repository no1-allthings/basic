# a=5
# b='5'
# print(a*b)
# print(b*a)
# print(int(12.9))
#
# num=5.5
# print(range(int(num)))
#
# g = input()
# print(g)

# y, m, d = map(int,input('yy.mm.dd: ').split('.'))
# print(y,m,d)
# print(type(y))
#
# g,h,j = list(map(int,input('세게 입력: ').split()))
# print(g,h,j)
# print(type(g))

# x=3
# y=5
# print(x,'과',y,'의 합',x+y,'이다')
# print(str(x)+'과'+str(y)+'의 합'+str(x+y)+'이다')
# print(x,end='')
# print('과',end='')
# print(y,end='')
# print('의 합',end='')
# print(x+y,     end='')
# print('이다')
#
# print(f'{x}과{y}의 합{x+y}이다')
#
# print(sum([5,7,]))


t = 'abcd efgh ijk'

# print(t[0])
# print(t[1])
# print(t[2])
# print(t[-3])
# print(t[-2])
# print(t[-1])

# te = 'abc {} {}'
# print(te.format('ABC','ABC'))
# te='abc ABC A.B.C'
# print(te.replace('ABC','A/B/C'))
# te='abc A/B/C A.B.C'
# a,b,c= te.split('.')
# print(a)
# print(b)
# print(c)

# ye = '%%%a%c***'
# print('*'.join(ye))
# print(ye.count('a'))
# print(ye.count('100'))
# ye = '%%%ab%c***'
# print(ye.strip('%'))
# print(ye.lstrip('%'))
# print(ye.rstrip('%'))

# hh = 'ABC ABC'
# print(hh.find('A'))
# print(hh.rfind('A'))
# print(hh.index('A'))
# print(hh.rindex('A'))

hd = 'A1a'
print(hd.isalpha())
print(hd.isalnum())
print(hd.isdigit())
print(hd.islower())
print(hd.isupper())
print(hd.isascii())
print(hd.isspace())
print(hd.istitle())

print(hd.upper())
print(hd.lower())

y='20'
m='1'
d='9'

print(y.zfill(4))
