# for i in range(1,11):
#     print(i, end="\n")

# num = int(input('입력: '))
# c=1
# while c<=num:
#     print(c, c**2)
#     c +=1


# n = int(input('숫자입력: '))
# if n == 1:
#     print('일')
# elif n == 2:
#     print('이')
# else:
#     print('삼')

# sum = 0
# while True:
#     cc = int(input('입력: '))
#     if cc<0:
#         break
#     else:
#         sum += cc
#     print(sum)

leap_year = None
year = int(input('년입력: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
else:
    leap_year = False

if leap_year:
    print(f'{year} leap year')
else:
    print(f'{year} not leap')