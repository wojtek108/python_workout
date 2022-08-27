def isint(item):
    try:
        int(item)
        return True 
    except ValueError:
        return False

def sumObjects(some_list):
    return sum(n for n in some_list if isint(n))


print(sumObjects([1, 2, 4, 'wg']))
print(sumObjects(['Wojtek', 'WG', 'costam']))
print(sumObjects([1.82, 7.38, 124789.7]))



