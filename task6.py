# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

a = list(map(float, input(:\n).split()))
a2 = [round(i % 1, 2) for i in a if i % 1 != 0]
print(max(a2) - min(a2))
