# the solution of the 'name triangle' exercise by Reuven Lerner.
# very neat!

def name_triangle():
    name = input('Enter your name: ')
    for i in range(len(name)):
        print(name[:i+1])

name_triangle()
