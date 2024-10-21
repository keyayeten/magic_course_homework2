# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму дробей.
# Ввод:
# 1/2
# 2/3
# Вывод:
# 7/6  (будет еще круче если упростите до 1+1/6)
num1 = list(map(int, input().split('/')))
num2 = list(map(int, input().split('/')))
znam1, znam2 = num1[1], num2[1]
num1 = [i*znam2 for i in num1]
num2 = [j*znam1 for j in num2]
result = num1[0] + num2[0]
if result > num1[1]:
    print(f'{result - num1[1]}+{result - num1[1]}/{num1[1]}')
else:
    print(f'{result}/{num1[1]}')
