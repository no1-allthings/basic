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

# n,m=list(map(int,input().split()))
#
# def prime(a):
#     if a<2:
#         return False
#     else:
#         for i in range(2,a):
#             if a % i == 0:
#                 return False
#         return True
#
# A =[]
# for i in range(n,m+1):
#     if prime(i):
#         A.append(i)
# print(A, len(A))
# dd = []
# def b_n(d):
#     while d>0:
#         d,m = divmod(d, 2)
#         dd.insert(0,m)
#
# b_n(13)
# print(dd)

# def a_p(*argument):
#     print(*argument)
#
# a_p(1,2,3,1)
#
# print(chr(65))
# print(ord('A'))
#
# print('hi bye'.split())

# txt = '''신경발달장애 Neurodevelopmental Disorders
# 조현병 스펙트럼 및 기타 정신병적 장애 Schizophrenia Spectrum and Other Psychotic Disorders
# 양극성 및 관련 장애 Bipolar and Related Disorders
# 우울장애 Depressive Disorders
# 불안장애 Anxiety Disorder
# 강박 및 관련 장애 Obsessive－Compulsive and Related Disorders
# 외상 및 스트레스 관련 장애 Trauma－and Stressor－Related Disorders
# 해리장애 Dissociative Disorders
# 신체증상 및 관련 장애 Somatic Symptom and Related Disorders
# 급식 및 섭식장애 Feeding and Eating Disorders
# 배설장애 Elimination Disorders
# 수면－각성 장애 Sleep－Wake Disorders
# 성기능부전 Sexual Dysfunctions
# 성별 불쾌감 Gender Dysphoria
# 파괴적, 충동조절 및 품행 장애 Disruptive, Impulse－Control, and Conduct Disorders
# 물질관련 및 중독 장애 Substance－Related and Addictive Disorders
# 신경인지장애 Neurocognitive Disorders
# 성격장애 Personality Disorders
# 변태성욕장애 Paraphilic Disorders
# 기타 정신질환 Other Mental Disorders'''
#
# disorders = dict()
#
# is_eng = lambda x: 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122
#
# for l in txt.split('\n'):
#     i = 0
#     while not is_eng(l[i]):
#         i += 1
#     else:
#         ko, en = l[:i - 1], l[i:]
#         disorders[ko] = en
#
# print(disorders)
#
#
# print(chr(122))

# a = list('goole')
# print(set(a))

d1=(1,2,3,4,5,6)
d2=(2,3,5,7,11,13)

d = set()
for x in d1:
    for y in d2:
        d.add(x+y)
print(d)