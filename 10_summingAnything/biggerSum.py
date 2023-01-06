def biggerSum(*items):
    if not items:
        return items
    benchmark = items[0]
    output = 0
    for item in items:
        if item > benchmark:
            output = output + item
    return output

print(biggerSum(4, 1, 2, 4, 5))
