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
# print(che)

nm = int(input('nn: '))
che = []
for i in range(2, nm):
    for j in range(2, i):
        if j % i != 0:
            che.append(j)
print(che)