numbers = 1.1, 1.2, 3.1, 5, 10.01
num = [i - int(i) for i in numbers]
lst = []
for i in num:
    lst.append(i)
max_num = max(lst)
min_num = min(lst)
print(max_num - min_num)