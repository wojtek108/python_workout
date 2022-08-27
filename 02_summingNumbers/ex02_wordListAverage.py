def wordList(lista):
    total = 0
    short = len(lista[0])
    long = len(lista[0])
    for word in lista:
        if len(word) < short:
            short = len(word)
        if len(word) > long:
            long = len(word)
        total = total + len(word)
        result = total/len(lista)
    return long, short, result

print(wordList(['tomek', 'michal', 'wg', 'gajewski']))

# https://github.com/reuven/python-workout/blob/master/ch01-numbers/e02b3_word_summary.py
# """Solution to chapter 1, exercise 2, beyond 3: words summary"""
# 
# 
# def summarize(words):
#     """Accepts a list of strings.
# Returns a 3-element tuple containing three integers: (a) length
# of the shortest word, (b) length of the longest word, and (c)
# average word length.
# """
#     word_lengths = [len(one_word)
#                     for one_word in words]
# 
#     return min(word_lengths), max(word_lengths), sum(word_lengths)/len(word_lengths)
