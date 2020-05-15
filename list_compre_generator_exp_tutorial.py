# # example of generator, using range(x):
# # instead of generator and storing a list in memory, it is iterating
# # for i in range(500):
# #     print(i)
# xyz = [i for i in range(50)]
# print('done')

# # generator expression
# # not storing a list just a generator object. Faster to make but slower later on 
# # when iterating since it is not stored in memory
# xyz = (i for i in range(50))
# print(xyz)

input_list = [5,6,2,1,6,7,10,12]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False
# making a generator of numbers in input list that are divisible by 5
xyz = (i for i in input_list if div_by_five(i))
# for i in xyz:
#     print(i)
xyz = [i for i in input_list if div_by_five(i)]
print(xyz)

# nested list comprehension for printing
# essentially a one line for loop
[[print(i,ii) for ii in range(5)] for i in range(5)]

xyz = [[i*ii for ii in range(5)] for i in range(5)]
print(xyz)

# storing functions in generator works too
xyz = (print(i) for i in range(5))
# when we iterate through the generator we dont call `print` again. just call `i` will do. 
for i in xyz:
    i