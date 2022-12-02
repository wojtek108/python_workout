def plus_minus(numbers):
    plus = []
    minus = []
    for number in range(len(numbers)):
        if number > 1 and number % 2 == 0:
            minus.append(numbers[number])
        else:
            plus.append(numbers[number])
    return sum(plus) - sum(minus)


lista = [10, 20, 40, 50, 80, 70]
some_tuple = (20, 30, 10, 70, 90, 120)

print(plus_minus(lista))
print(plus_minus(some_tuple))

# the solution by Reuven below does not work with tuples!
# pop() method applies to list only!

def plus_minus1(numbers):

    if not numbers:
        return 0
    total = numbers.pop(0)
    while numbers:
        total += numbers.pop(0)
        if numbers:
            total -= numbers.pop(0)
    return total

print(plus_minus1(lista))
