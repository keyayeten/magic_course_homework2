lst = ['Hello', 1, '7', True, False, 5.4]


stroka = []
booling = []
integer = []
floatter = []
for i in lst:
    if type(i) == str:
        stroka.append(i)
    elif type(i) == bool:
        booling.append(i)
    elif type(i) == int:
        integer.append(i)
    elif type(i) == float:
        floatter.append(i)
total = f'str: {stroka}, bool: {booling}, int{integer}, float: {floatter}'
print({total})








