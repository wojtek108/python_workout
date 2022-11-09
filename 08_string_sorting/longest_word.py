with open('the_zen_of_python.txt') as f:
    contents = f.read()
    words_list = contents.split()
    words_lenght_list = [len(x) for x in words_list]
    list_sorted = sorted(words_lenght_list)
    print(list_sorted[-1])

