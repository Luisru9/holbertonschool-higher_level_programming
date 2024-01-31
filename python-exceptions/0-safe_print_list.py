#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    if not my_list or x == 0:
        print()
        return 0

    try:
        printed_elements = [str(element) for element in my_list[:x]]
        print("".join(printed_elements))
        return len(printed_elements)
    except (IndexError, TypeError):
        print()
        return len(printed_elements)
