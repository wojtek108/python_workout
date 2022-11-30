file = open('test.txt')
print(type(file)) # a text wrapper object
print(type(file.readlines())) # a list


print(2222222222222)
file = open('test.txt')
for one_line in file:
    print(one_line)
print(5555555555555)
file = open('test.txt')
for one_line in file.readlines():
    print(one_line)

print(88888888888888)
file = open('test.txt')
content_list = file.readlines()
for one_line in content_list:
    print(one_line)

'''
with open('test.txt') as f:
    contents = f.readlines()
    print(contents)
f = open('test.txt')
content = f.readlines()
for line in content:
    print(line)

'''
