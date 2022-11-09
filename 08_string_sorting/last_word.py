with open('the_zen_of_python.txt') as f:
    contents = f.read()
    words_list = contents.split()
    print(sorted(words_list)[-1])
