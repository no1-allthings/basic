# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# print()
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)
# print()
# for i in range(5):
#     if i ==3:
#         pass
#     print(i)

# a = int(input('나이입력: '))
# if a>=20:
#     print('성인')
# elif 7<a<=19:
#     print('청소년')
#     if a<=13:
#         print('초등')
#     elif a<=16:
#         print('중등')
#     else: print('고등')
# else:
#     print('유아')

# n = int(input('n: '))
# for i in range(1,n+1):
#     if i % 3 == 0:
#         print('x')
#     else: print(i)
#
# num = 0
# n2=int(input('ne: '))
# while True:
#     print(num)
#     num+=1
#     if num == n2:
#         break

s = set()
for i in range(1,7):
    for j in range(1,7):
        s.add(i+j)
print(s)