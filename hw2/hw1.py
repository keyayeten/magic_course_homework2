# ls = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# ls = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# ls = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
ls = ["abc", "cde", "def", "cde", "abc"]
d = {}
for vales in ls:
    if vales in d:
        d[vales] += 1
    elif vales not in d:
        d[vales] = 1

for k, v in d.items():
    if v == 2:
        print(k, v)
        break
    else:
        print(-1)




