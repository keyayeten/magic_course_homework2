from fractions import Fraction

a = input()
b = input()

#Убираем '/'
str1 = a.split('/')
str2 = b.split('/')

num1 = [int(i) for i in str1]
num2 = [int(i) for i in str2]
print(Fraction(num1[0], num1[1]) + Fraction(num2[0], num2[1]))



