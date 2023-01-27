def sortBySum(lists):
    return sorted(lists, key = sum)

test = [[1, 2, 3], [11, 12, 14], [7, 8, 9], [5, 6, 7]]

print(sortBySum(test))
