import operator

MOVIES = [('Parasite', 132, 'Bong Joon-ho'),
          ('Ford v Ferrari', 152, 'James Mangold'),
          ('The Irishman', 209, 'Martin Scorsese'),
          ('Jojo Rabbit', 108, 'Taika Waititi'),
          ('Joker', 122, 'Todd Phillips'), 
          ('Little Women', 135, 'Greta Gerwig'),
          ('Marriage Story', 137, 'Noah Baumbach'),
          ('Once Upon a Time in Hollywood', 161, 'Quentin Tarantino')]

FIELDS = {'name': 0,
          'length': 1,
          'director': 2}
def sort_movies():
    sort_by = input('Enter sort field, separte by " " for multiple fields: (name/lenght/director): ').split()
    if all(item in FIELDS for item in sort_by):
        output = []
        template = '{0:30} {1:8} {2:20}'
        for one_movie in sorted(MOVIES, key = operator.itemgetter(*[FIELDS[item] for item in sort_by])):
            output.append(template.format(*one_movie))
        return output
    print(f'No such field as {sort_by}')  



print('\n'.join(sort_movies()))

