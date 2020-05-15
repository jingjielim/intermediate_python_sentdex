names = ['Jeff', 'Gary', 'Jill', 'Samantha']

# for name in names:
#     # Two different ways to print all the names
#     print('Hello there, ' + name)
#     # .join takes less processing power. i.e. always use .join
#     print(' '.join(['Hello there,', name]))

# print(', '.join(names))

## Concatenating filenames
# import os

# location_of_file = '/Users/JingJie/Desktop/GitHub/intermediate_python_youtube'
# filename = 'example.txt'
# with open(os.path.join(location_of_file, filename)) as f:
#     print(f.read())

# String formatting
who = 'Gary'
how_many = 12
# Gary bought 12 apples today
# Wrong way of doing this:
print(who, 'bought', how_many, 'apples today!')
# Correct way of doing this
print('{} bought {} apples today!'.format(who, how_many))