def latin_pig(word):
    if word[0] in 'aieouAIEOU':
        return f'{word}way'
    if word[0].isupper():
        return f'{word[1:].capitalize() + word[0].lower()}ay' 
    else:
        return f'{word[1:] + word[0]}ay'

print(latin_pig('uojtek'))
