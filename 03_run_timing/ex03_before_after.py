def beforeafter(float_number, before, after):
    string = str(float_number)
    digits_before, point, digits_after = string.partition('.')
    list_int = list(digits_before)
    list_float = list(digits_after)
    output_before = list_int[before:]
    output_after = list_float[:-after]
    result = ''.join(output_before + ['.'] + output_after)

    return(float(result))

print(beforeafter(12345.12345, 3, 4))


