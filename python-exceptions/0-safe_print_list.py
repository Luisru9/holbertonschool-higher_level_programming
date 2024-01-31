#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    count_elements = 0
    try:
        for element in my_list:
            if count_elements < x:
                print("{}".format(element), end="")
                count_elements += 1
            else:
                break
    except TypeError:
        pass
    finally:
        print()
    return count_elements
