# l3 = [1,2,3,10,20,30]
# l3.sort()
#
# f = int(input('f1:'))

# for i in range(len(l3)):
#     if l3[i]==f1:
#         print(i)
#         break


# s = 0
# e = len(l3)-1
#
# while s<=e:
#     m=(s+e)//2
#     if f > l3[m]:
#         s=m+1
#     elif f< l3[m]:
#         e=m-1
#     else:
#         print(m)
#         break


#선택정렬
l=[2,4,5,1,3,7,9,6,8,10]

# for i in range(len(l)-1):
#     print(l)
#     min_i = i
#     for j in range(i+1,len(l)):
#         if l[j]<l[min_i]:
#             min_i=j
#     l[i], l[min_i]= l[min_i], l[i]
    #print(l)

# for i in range(len(l)):
#     print(l)
#
#     temp = i
#     for j in range(i+1,len(l)):
#         if l[j]<l[temp]:
#             temp=j
#     l[temp],l[i]=l[i],l[temp]
#     print(l)
# print(l)

#버블정렬
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
    print(l)

