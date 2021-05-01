# family = ['father', 'mother', 'i', ]
#
# for i in family:
#     print(len(family), i, len(i))
# s= range(2,7)
# print(list(s))
#
# ss= int(input('입력: '))
# for i in range(ss):
#     print(i,ss)

# aa = int(input('입:'))
# for i in range(1,aa+1):
#     print(i, i*i)


min, max = map(int, input('두개입력:').split())
tmp = list(map(int,input().split()))

for i in tmp:
    if min<= i <= max: print('nothings')
    elif i == -999 : break
    else:
        print('경고')
        break