# for a in range(2,10):
#     print(f'[{a}  단]')
#     for b in range(1,10):
#         print(f'{a}*{b}={a*b:2d}')
#     print('--------')
#
# def multi(m):
#     for n in range(1, 10):
#         print(f'{m} * {n} = {m*n:2d}')
#
# multi(3)

# def tri(a,b):
#     c= a*b/2
#     return c
# d=tri(2,2)
# print(d)
#
# def n_k(x):
#     dict = {1:'일', 2:'이', 3:'삼'}
#     if x in dict:
#         return (dict[x])
# y =n_k(3)
# print(y)


# def s_i(p,r,t):
#     return ('이자는 ' +str(p*r*t), '원리금은 ' +str(p*(1+r*t)))
# #if __name__ == '__main__':
# print(s_i(1,2,3))
#
# def c_i(p,r,t,n):
#     return p*(1+r/n)**(t*n)
# print(c_i(1500000,0.043, 6, 4 ))

x = (lambda a,b :a+b) (1,2)
print(x)

u=list(map(lambda x:x**2,range(5)))
print(u)

y=[]
for i in range(5):
    y.append(i**2)
print(y)

from functools import reduce
users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M', 'age': 73},
    {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F', 'age': 29},
    {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M', 'age': 51},
    {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F', 'age': 32},
    {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F', 'age': 42}]
p=reduce(lambda a, c: a + c["age"], users, 0)
print(p)
m=reduce(lambda acc, cur: acc + [cur["mail"]], users, [])
print(m)

j= list(filter(lambda m:m>5,range(10)))
print(j)