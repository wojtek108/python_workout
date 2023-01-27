
def maxVowels(string):
    start = 0
    for letter in string.lower():
        if letter in 'aeiou':
            start = start + 1
    return start


def stringList(strings):
    return sorted(strings, key = maxVowels)

a = ['some', 'a', 'somemore']

print(stringList(a))


"""
https://scribe.rip/analytics-vidhya/sorted-function-using-key-parameter-in-python-7aa9b8cebfb6
https://note.nkmk.me/en/python-key-sort-sorted-max-min/
https://scribe.rip/towardsdatascience.com/sorting-lists-in-python-31477e0817d8
https://scribe.rip/levelup.gitconnected.com/sorting-in-python-using-keys-d2622edd7a92
"""
