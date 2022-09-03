def pig_latin(word):
    letters = set(word)
    vowels = {'a', 'i', 'e', 'o', 'u', 'y'}

    if len(letters.intersection(vowels)) > 1:
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

print(pig_latin('wojtk'))
        
