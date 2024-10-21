# Создайте вручную список содержащий элементы разных типов.
# Получите из него словарь списков, где ключ - тип элемента,
# а значение - список элементов данного типа.
# Для списка: [1, 2, "3", "4", True, 5.5]
# Ответ:  {int: [1, 2, 5], float: [5.5], str: ["3", "4"], bool: [True]}

# решение 1
elements = [1, 2, "3", "4", True, 5.5]
type_list = {
    'int': [],
    'float': [],
    'str': [],
    'bool': []
}
for i in elements:
    if type(i) is int:
        type_list['int'].append(i)
    elif type(i) is float:
        type_list['float'].append(i)
    elif type(i) is str:
        type_list['str'].append(i)
    elif type(i) is bool:
        type_list['bool'].append(i)
print(type_list)

# решение 2

elements = [1, 2, "3", "4", True, 5.5]
type_list = {
    int: [],
    float: [],
    str: [],
    bool: []
}
for i in elements:
    type_list[type(i)].append(i)
print(type_list)