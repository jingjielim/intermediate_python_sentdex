example = ['left', 'right', 'up', 'down']

# Wrong way of doing it
# Looks ridiculous to range(len(x))
for i in range(len(example)):
    print(i, example[i])
# Correct way of doing it
# can enumerate over a dictionary
for index, value in enumerate(example):
    print(index, value)

new_dict = dict(enumerate(example))
print(new_dict)
