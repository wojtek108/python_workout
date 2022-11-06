def name_sort(names):
    words_list = text.split(' ')
    words_list.sort()
    return ', '.join(words_list)


text = 'Tom Dick Harry'

print(name_sort(text))

