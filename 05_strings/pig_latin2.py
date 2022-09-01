def latin_pig(word):
    if word[0] in 'aieou':
        return str(word +'way')
    return str(word[1:] + word[0] + 'ay')

print(latin_pig('wojtek'))
