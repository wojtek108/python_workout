def remove_names(text, names):

    output01 = text
    output02 = [] 
    for name in names:
        new_name = name.replace(name, '_' * len(name))
        output02.append(new_name)
    return output01, output02  


print(remove_names('some title', ['wg', 'tt']))
