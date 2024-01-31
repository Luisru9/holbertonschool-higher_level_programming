#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list or x == 0:
        print()
        return 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
        print()
        return i + 1
    except (IndexError, TypeError):
        print()
        return i
