# l1 = input('문자 :').split()
# print(l1)
#
# l2=list(input('문자'))
# print(l2)

l3=[]
# l3.append(int(input('숫자')))
# # l3.extend(input('문자').split())
# # l3.append((input('문자')))
# # l3.append(input('문자').split())
#l3.insert(0,1)

l3 = list(map(int, input('입력:').split()))
print(l3)

l3.sort()
print(sum(l3))
print(sum(l3)/len(l3))
print(l3[0]) #최소값
print(l3[len(l3)-1])
print(l3[len(l3)//2]) # 중간값