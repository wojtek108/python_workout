def mysum(*numbers):
    output = 0
    for number in numbers:
        output = number + output
    return output

print(mysum(1, 2, 5, 88))
