#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    if not my_list or x == 0:
        print()
        return 0
    i = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            # Check for IndexError and break if needed
            if i >= len(my_list) - 1:
                break
    except TypeError:
        pass
    finally:
        print("")
    return i + 1
