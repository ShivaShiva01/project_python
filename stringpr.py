a_list = ['xerox', 'boss', 'shiva', 'gaddam', 'Karanam', '12abc']
a_word = "Banigandlapadu"


# b_list = a_list.sort()

def last_fun(s):
    return s[-2]


b_list = sorted(a_list, key=last_fun)
print(b_list)
