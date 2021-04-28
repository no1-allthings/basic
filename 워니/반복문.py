for i in range(3):
    print(i)
    print('hi')

i = 0
while i <3:
    print(i)
    print('hi')
    i += 1

for i in range(500):
    if i < 480:
        continue
    print(i)
    print('bye')

    if i >= 481:
        break