# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

a_list = ['aa', 'xx', 'zz']
b_list = ['bb', 'cc']

a_list.extend(b_list)
a_list.sort()

# result_1 = []
#
# while len(a_list) and len(b_list):
#     if a_list[0] < b_list[0]:
#         result_1.append(a_list.pop(0))
#
#     else:
#         result_1.append(b_list.pop(0))

