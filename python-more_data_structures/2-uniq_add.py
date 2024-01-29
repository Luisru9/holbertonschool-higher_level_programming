#!/usr/bin/python3
def uniq_add(my_list=[]):
    total_sum = 0

    unique_set = set()

    for number in my_list:
        if number not in unique_set:

            total_sum += number
            unique_set.add(number)

            return total_sum
