from fractions import Fraction

a = input()
b = input()

#Убираем '/'
str1 = a.split('/')
str2 = b.split('/')

num1, num2 = map(int, str1)
num3, num4 = map(int, str2)
print(Fraction(num1, num2) + Fraction(num3, num4))



