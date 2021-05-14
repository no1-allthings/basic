# l1 = []
# for i in range(4):
#     l1.append(int(input('숫자')))
# for i in l1:
#     if i % 2 == 0:
#         print(i)
#
# print()
#
# for i in range(len(l1)):
#     if i % 2 ==0:
#         print(l1[i])

up=[]
lo=[]
etc=[]
l=list(input('문자열: '))

for i in l:
    if i.isupper():
        up.append(i)
    elif i.islower():
        lo.append(i)
    else:
        etc.append(i)
print(up, lo, etc)