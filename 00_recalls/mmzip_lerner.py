# try to comprehend the function below:

def myzipy(*args):
    """Takes any number of iterables, returning
a list of tuples. The tuple at index n will contain
the items from index n in each iterable.  We can
assume that all of the iterables have the same length.
"""
    return [tuple(a[i] for a in args) for i in range(len(min(args, key=len)))]



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

print(myzipy(a, b, c, d))
print(myzip(a, b, c, d))

