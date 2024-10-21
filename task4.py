# Создайте вручную список содержащий элементы разных типов.
# Получите из него словарь списков, где ключ - тип элемента,
# а значение - список элементов данного типа.
# Для списка: [1, 2, "3", "4", True, 5.5]
# Ответ:  {int: [1, 2, 5], float: [5.5], str: ["3", "4"], bool: [True]}
elements = [1, 2, "3", "4", True, 5.5]
type_list = {}    
for i in elements:
    if type(i) not in type_list:
        type_list[type(i)] = []
    type_list[type(i)].append(i)
print(type_list)