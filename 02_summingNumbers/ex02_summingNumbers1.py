# similar to summingNumbers.py but now mysum() accepts also tuples and lists of ints for calculating total

def mysum(*numbers):
    output = 0
    for number in numbers:
        if type(number) in [list, tuple]:
            s = 0
            for n in number:
                s = n + s
            number = s
        output = number + output
    return output

print(mysum(1, [2, 4], 5, 88, (10, 20, 30, 40)))
