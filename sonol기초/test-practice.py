# def ff(x,y):
#
#     if x<=y:
#         print('stop')
#     elif x % y == 0:
#         print('true')
#     else: print('false')
# ff(3,8)

# li = list(map(int, input('n').split()))
# m = int(input('m'))
# check =False
#
# for i in li:
#     if i == m:
#         check=True
# print(check)

# n = int(input('n'))
# check = 0
# ls = []
# for i in range(1,n+1):
#     if n % i == 0:
#         check +=1
#         ls.append(i)
# print(check)
# print(ls, len(ls), sum(ls))

# te= list(input('입력: '))
# o_c = 0
# x_c = 0
# for i in te:
#     if i == 'o':
#         o_c += 1
#     elif i == 'x':
#         x_c += 1
# print(o_c, x_c)
# print(te.count('o'))
# print(te.count('x'))

# nu = list(map(int, input('nu').split()))
# av = sum(nu)/len(nu)
# co=0
# for i in nu:
#     if i >av:
#         co +=1
# print(co)

# jj = int(input('jj'))
# che = []
# for i in range(1,jj+1):
#     if jj % i == 0:
#         che.append(i)
# if len(che)>2:
#     print(False)
# else: print(True)

# nn = int(input('nn: '))
# che = True
# for i in range(2, nn):
#     if nn % i == 0:
#         che = False
# if True:
#     print('소수')
# else: print('no')

# nm = int(input('nn: '))
# che = []
# for i in range(2, nm+1):
#     c = True
#     for j in range(2, i):
#         if i % j == 0:
#             c=False
#     if c:
#         che.append(i)
# print(che, len(che))

# n=int(input('n: '))
# r=3
# for i in range(n-1):
#     r=r+5
# print(r)
#


# m=int(input('m: '))
# r=1
# f=1
#
# for i in range(m-2):
#     c=r+f
#     r=f
#     f=c
# print(f)

# for i in range(5):
#     print(' ' * i+'*'*5)
    # print(' '*i, end='')
    # print('*'*5)
#
# for i in range(1,4):
#     print(' '*(4-i),end='')
#     print('*'*i)

# n=int(input('n :'))
# for i in range(n):
#     print(' '*(n-i-1), end='')
#     print('*'*(i*2+1))

# for i in range(2,10):
#     print(f'{i}단 시작')
#     for j in range(1,10):
#         print(f'{i}*{j}={i*j}')
#     print('***********')

# f=set()
# for i in range(1,7):
#     for j in range(1,7):
#         f.add(f'{i+j}')
# print(len(f),f)

l9 = [[1,2,3,4],[5,6,7,8]]
for i in range(len(l9)):
    #print(i)
    for j in range(len(l9[i])):
        print(l9[i][j], end='')
    print()



l=[11,12,13]
for h in l:
    print(h, end=' ')