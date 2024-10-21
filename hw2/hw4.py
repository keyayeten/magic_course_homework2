lst = ['Hello', 1, '7', True, False, 5.4, (1,)]
d = {'int': [], 'str': [], 'float': [], 'bool': [], 'tuple': []}
strs = []
ints = []
floats = []
bools = []
tuples = []
for i in lst:
    if type(i) == str:
        strs.append(i)
        d['str'] = strs
    elif type(i) == int:
        ints.append(i)
        d['int'] = ints
    elif type(i) == float:
        floats.append(i)
        d['float'] = floats
    elif type(i) == bool:
        bools.append(i)
        d['bool'] = bools
    elif type(i) == tuple:
        tuples.append(i)
        d['tuple'] = tuples
print(d)
dicts = {k: v for k, v in d.items() if v}
print(dicts)










