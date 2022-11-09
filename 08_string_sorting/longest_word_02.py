def longest(file):
    output = ''
    for one_line in open(file):
        for one_word in one_line.split():
            if not one_word.isalpha():
                continue
            if len(one_word) > len(output):
                output = one_word
    return output

print(longest('the_zen_of_python.txt'))
