# # introducing `yield` keyword
# def simple_gen():
#     yield 'Oh'
#     yield 'hello'

# # prints out 'Oh' then 'hello'
# for i in simple_gen():
#     print(i)

CORRECT_COMBO = (3, 6, 1)
# # using for loops, we have to set another variable to break the loop all the way through
# found_combo = False
# for c1 in range(10):
#     if found_combo:
#         break
#     for c2 in range(10):
#         if found_combo:
#             break
#         for c3 in range(10):
#             if (c1, c2, c3) == CORRECT_COMBO:
#                 print('Found the combo {}'.format((c1,c2,c3)))
#                 found_combo = True
#                 break
#             print(c1, c2, c3)

# we can use a generator instead
# looks better and doesn't waste memory
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for combo in combo_gen():
    print(combo)
    if (combo == CORRECT_COMBO):
        print('Found the combo {}'.format(combo))
        break