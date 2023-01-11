
def isInt(items):
    output = []
    for item in items:
        try:
            int(item)
            output.append(int(item))
        except ValueError:
            pass
    return sum(output)

someVar = (1, -2, '2', '-3', 'wa')

print(isInt(someVar))
