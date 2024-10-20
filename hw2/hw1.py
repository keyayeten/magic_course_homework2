# ls = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
ls = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# ls = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]


index = 0 #счетчик подсчета индекса в списке
lst = []
for i in ls:
    if i not in lst:
        lst.append(i)
        index += 1
    else:
        print(f'ищем {str(i)}, ответ {index}')
        break
else:
    print(-1)







