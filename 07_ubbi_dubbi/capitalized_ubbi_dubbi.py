def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in 'aeiouAEIOU':
            output.append(f'ub{letter}')
        else:
            output.append(letter)

    string = ''.join(output)

    if word[0].isupper():
        return string[0].upper() + string[1:].lower()
    else:
        return string


print(ubbi_dubbi('Wojtek'))

