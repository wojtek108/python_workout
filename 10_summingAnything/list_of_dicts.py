
def listDict(dictionaries):
    keys = []
    values = []
    for n in range(len(dictionaries)):
        for key in dictionaries[n]:
            keys.append(key)
        for value in dictionaries[n].values():
            values.append(value)

    singleKeys = []
    for key in keys:
        if key not in singleKeys:
            singleKeys.append(key)

    alist = []
    for singleKey in singleKeys:
        blist = []
        for number, value in enumerate(keys):
            if singleKey == value:
                blist.append(values[number])
        alist.append(blist)

    dlist = [n if len(n) > 1 else n[0] for n in alist]

    output = dict(zip(singleKeys, dlist))
    return output 




dicts = [{'a': 'b', 'c': 'd'}, {'a': 1, 'f': 'g', 'h': 'i'}, {'2': 1, '5': 'wg'}, {'a': 'abc', 'f': 'chess'}]
di = [{'a': 'b', 'c': 'd'}, {'a': 1, 'f': 'g', 'h': 'i'}, {'a': 1, 'f': 'g', 'h': 'i'}, {'2': 1, '5': 'wg'}, {'a': 'abc', 'f': 'chess'}]

print(listDict(dicts))
print(listDict(di))
