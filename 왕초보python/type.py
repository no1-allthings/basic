# o="seguence"
# print(o[:])
# print(o[::-1])
# print(o[:-2])
# print(o[-2:])
# print(o[0:5:2])
# print(o[:5])
# print(o.replace('e','a'))
# print(o.upper())

#
# def ppp(s):
#     s = s.lower()
#     s = s.replace(" ","")
#     return s == s[::-1]
# for i in ['anna', 'banana', 'Anna', 'My gym', 'sfkgl',]:
#     if ppp(i):
#         print("yes")
#     else:
#         print("no")

# pp = [1,3,5,]
# pp.append(7)
# pp.insert(0,9)
# pp.sort()
# del pp[2]
# pp[0]=0
# print(pp)
#
# jj = [1,3,[2,4,6],5,]
# print(jj[2][0])
#
# ff = 'se quence'
# print(list(ff))
#
# ll =[]
# for l in ff:
#     ll.append(l)
# print(ll)

# gg = '123'
# print(int(gg))
#
# ww = list(range(11))
# print(sum(ww))

# yo = [50,50,50]
# ch = [60,60,60]
# de = [70,70,70]
#
# sss = [yo, ch, de]
#
# for i in sss:
#
#     sum = 0
#     for d in i:
#
#         sum += d
#     ave = sum/3
#     print(f'{i}의 총점: {sum} 평균: {d}')

# aa = list(map(int, input('정수입력: ')))
# print(sum(aa))

# def su(num):
#     mm=0
#     for i in list(str(num)):
#         print(i,type(i))
#         mm += int(i)
#         print(type(mm))
#     return mm
#
# print(su(123))

# score = [0,0,2,4,7,7,9]
# score += [11,11,13,18]
# score += [20]
#
# stem_leaf = [[],[],[]]
# for i in score:
#     d,m = divmod(i,10)
#     stem_leaf[d].append(m)
# print(stem_leaf)
#
# for i in range(len(stem_leaf)):
#     print(f'{i} {stem_leaf[i]}: ')

# print((643%10)+(643// 10))
#
# def sd(num):
#     hab = list(map(int, str(num)))
#     return sum(hab)
# print(sd(123))
#
# def sumd(num):
#     sum = 0
#     while num>=1:
#         sum += num%10
#         num //=10
#     return sum
# print(sumd(123))

n,m=list(map(int,input().split()))

def prime(a):
    if a<2:
        return False
    else:
        for i in range(2,a):
            if a % i == 0:
                return False
        return True

A =[]
for i in range(n,m+1):
    if prime(i):
        A.append(i)
print(A, len(A))







