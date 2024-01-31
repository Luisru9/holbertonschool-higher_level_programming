#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    try:
        for element in my_list[:x]:
            print(element, end="")
    except IndexError:
        pass
    finally:
        print()
    return min(x, len(my_list))
