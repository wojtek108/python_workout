# active recall of previous script

def last_word(filename):
    output = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if not one_word.isalpha():
                continue
            if one_word > output:
                output = one_word
    return output

print(last_word('test'))


        
def longest_word(filename):
    output = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if not one_word.isalpha():
                continue
            if len(one_word) > len(output):
                output = one_word
    return output

print(longest_word('test'))


        
