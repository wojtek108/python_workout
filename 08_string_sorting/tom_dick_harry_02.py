def name_sort(names):
    words_list = text.split(' ')
    new_list = sorted(words_list)
    return ', '.join(new_list)


text = 'Tom Dick Harry'

print(name_sort(text))

