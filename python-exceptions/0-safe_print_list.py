#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    count_elements = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end=' ')
            count_elements += 1
    except IndexError:
        pass
    finally:
        print()
    return count_elements
