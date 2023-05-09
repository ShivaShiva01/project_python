# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.

a_list = ['apple', 'bob', 'no', 'nan', 'just', 'roar', 'welcome']
b_list = ['aba', 'xyz', 'aa', 'x', 'bbb']
count = 0
for name in a_list:
    if name[0] == name[-1]:
        count += 1
print(count)

# adding condition to check length is greater then or equal to 2

count_1 = 0
for name_1 in b_list:
    if name_1[0] == name_1[-1] and len(name_1) >= 2:
        count_1 += 1

print(count_1)



