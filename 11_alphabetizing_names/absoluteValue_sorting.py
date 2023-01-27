def absoluteValue(numbers):
    return sorted(numbers, key = abs)


a = (-7, 6, -2, 8, 2, -9)

print(absoluteValue(a))
