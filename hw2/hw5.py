import re

# text = list(map(str, input().split()))
text = 'She sells sea shells on the sea shore; The shells that she sells are sea shells Im sure.So if she sells sea shells on the sea shore,Im sure that the shells are sea shore shells.'

#Убираем все лишние символы и преобраз. в малый регист
t = re.sub('[!@#-.;:,]', '', text).lower()
#Словарь
d = {}

for vales in str(t).split():
    if vales in d:
        d[vales] += 1
    else:
        d[vales] = 1
print(d)

#Сортировка по значению
d_sort = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print(d_sort)
val = list(d_sort.keys())
print(*val[0:10])
