def hex_output():
    decsum = 0
    hexsum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexsum)):
        decsum = decsum + int(digit, 16) * (16 ** power)
    print(decsum)

hex_output()
