# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
from operator import itemgetter, attrgetter

a_list = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]


def last(a):
    return a[-1]


print(sorted(a_list, key=last))
