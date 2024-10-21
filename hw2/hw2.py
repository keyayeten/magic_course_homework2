lst = list(map(int, input().split(',')))

summa = 0
for index, values in enumerate(lst):
    if index % 2 != 0:
        summa += values
print(summa)


