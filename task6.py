# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
spk = [1.1, 1.2, 3.1, 5, 10.01]
new_spk = []
for i in spk:
    if i - int(i) != 0:
        new_spk.append((i - int(i)))
num_min = min(new_spk)
num_max = max(new_spk)
res = abs((num_max - int(num_max)) - (num_min - int(num_min)))
print(f'{res:.2f}')