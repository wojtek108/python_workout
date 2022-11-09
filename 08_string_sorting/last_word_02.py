def last_word(file):
    output = ''
    for one_line in open(file):
        for one_word in one_line.split():
            if not one_word.isalpha():
                continue
            if one_word > output:
                output = one_word

    return output   
print(last_word('the_zen_of_python.txt'))



