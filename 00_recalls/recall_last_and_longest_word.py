def lastword(file):
    output = ''
    for one_line in open(file):
        for one_word in one_line.split():
            if not one_word.isalpha():
                continue
            if one_word > output:
                output = one_word
    return output

print(lastword('test'))

'''
with open('test') as f:
    contents = f.readlines()
    print(contents)

'''


def longestword(file):
    output = ''
    for one_line in open(file):
        for one_word in one_line.split():
            if not one_word.isalpha():
                continue
            if len(one_word) > len(output):
                output = one_word
    return output

print(longestword('test'))
