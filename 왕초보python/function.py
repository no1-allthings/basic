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


def s_i(p,r,t):
    return ('이자는 ' +str(p*r*t), '원리금은 ' +str(p*(1+r*t)))
#if __name__ == '__main__':
print(s_i(1,2,3))