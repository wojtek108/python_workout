def myzip(*iterables):
    turnedList = list(iterables)
    items = len(iterables)
    result = []
    for n in range(len(iterables[0])):
        output = []
        for m in range(items):
            output.append((turnedList[m][n]))
        b = tuple((output))
        result.append(b)
    return result



a = '12345'
b = 'abcde'
c = ['xx', 'yy', 'zz', 'aa', 'bb']
d = (11, 22, 33, 44, 55)

print(myzip(a, b, c, d))
