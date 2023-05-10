#D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

a_list = [1, 2, 2, 3,4,4,5]
b_list = []
for item in range(len(a_list)-1):
    if a_list[item] == a_list[item+1]:
        b_list.append(a_list[item])

for i in range(len(b_list)):
    a_list.remove(b_list[i])

print(a_list)




