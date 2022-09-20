a = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz', '123 456 789', 'aaa bbb ccc']

def transpose(alist):
    blist = [elem.split() for elem in alist]
    clist = list(zip(*blist))
    return [' '.join(elem) for elem in clist]
print(transpose(a))
