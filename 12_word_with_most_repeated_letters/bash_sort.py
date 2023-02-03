import operator
from collections import Counter

def shell_freq(filename):
    shells = Counter(one_line.split(':')[-1].strip() 
            for one_line in open(filename)
            if not one_line.startswith(('#', '\n')))

    return sorted(shells.items(), key = operator.itemgetter(1), reverse = True)

print(shell_freq('abc.txt'))
