x = [1,2,3,4]
y = [7,8,3,2]
z = ['a','b','c','d']

# # zip makes a zip object
# # zip object is iterable
# print(list(zip(x,y,z)))

# for i in zip(x,y,z):
#     print(i)

# zip with list comprehensions
[print(a,b,c) for a,b,c in zip(x,y,z)]

# variables in a for loop are stored
# variable `x` is being overwritten
for x,y in zip(x,y):
    print(x,y)
# `x` is no longer a list
print(x)
