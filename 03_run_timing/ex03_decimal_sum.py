from decimal import Decimal

def sum_float(a, b):
    return float(Decimal(a) + Decimal(b))

x = input('give me a float: ')
y = input('give me another float: ')

print(sum_float(x, y))
