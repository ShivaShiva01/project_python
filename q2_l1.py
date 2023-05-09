# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

a_list = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
b = []
print(a_list)
for name in a_list:
    if name[0] == 'x':

        b.append(name)
        a_list.remove(name)


a_list.sort()
b.sort()
b.extend(a_list)
print(b)

