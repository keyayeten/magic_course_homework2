lst = list(map(int, input().split(',')))

list_spisok = []
for index, values in enumerate(lst):
    if index % 2 != 0:
        list_spisok.append(values)
print(list_spisok)

#Подсчитываем сумму
summa = 0
for i in list_spisok:
    summa += i
print(summa)
