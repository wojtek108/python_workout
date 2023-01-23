import operator

get_2_and_4 = operator.itemgetter(2, 4)
s = 'abcdef'
t = (10, 20, 30, 40, 50)

print(get_2_and_4(s))
print(get_2_and_4(t))
