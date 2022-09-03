def pig_latin(word):
    punctuation = ''

    if word[-1] in '.?!,:;_–':
        punctuation = word[-1]
        word = word[:-1]
    
    if word[0] in 'aeiou':
        output = f'{word}way'
        return output + punctuation     
    else:
        output = f'{word[1:]}{word[0].lower()}ay'
        return output + punctuation

print(pig_latin('Python!'))

