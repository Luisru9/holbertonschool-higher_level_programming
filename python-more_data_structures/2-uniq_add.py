#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    res = 0
    for i in range(len(my_list)):  # for i in my_list:
        if my_list[i] not in my_list[:i]:  # if i not in my_list[:i]:
            res += my_list[i]  # sum value to total
    return res
