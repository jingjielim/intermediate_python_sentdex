# example of generator, using range(x):
# instead of generator and storing a list in memory, it is iterating
# for i in range(500):
#     print(i)
xyz = [i for i in range(50000000)]
print('done')
# generator expression
# not storing a list just a generator object. Faster to make but slower later on 
# when iterating since it is not stored in memory
xyz = (i for i in range(50000000))
print(xyz)