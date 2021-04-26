z=(4,5,6,)
print(type(z))

num1, num2, num3 = z
print(num1, num2, num3)
num1, num3 = num3, num1
print(num1, num2)
print(num1, num2, num3)