# def chat(a,b,d):
#
#     print("%s: 안녕 너 몇살이니"%a)
#     print("%s:나는 %d" %(b,d))
#
# chat("영희", "철수", 20)
#
# def dsum(x,y):
#     r = x+y
#     return r
# print(dsum(1,2))

def say(name, age):
    if age <10:
        print('안녕 '+ name)
    elif age>=10 and age <=20:
        print('반가워 '+name)
    else:
        print('안녕하세요 '+name)

say('영희', 20)
say('지아', 9)
say('철수', 32)