from collections import Counter

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example_exapmle_example']



def most_repeating_letter_count(word):
    new_word =' '
    for letter in word.lower():
        if letter in 'aeiouy':
            new_word = new_word + letter
    output = Counter(new_word).most_common(1)[0][1]
    return output 


def most_repeating_word(words):
    return max(words, key = most_repeating_letter_count)

print(most_repeating_word(WORDS))
