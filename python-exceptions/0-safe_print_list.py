#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i])
    except IndexError:
        print("IndexError: The list does not have enough elements.")
        return "Not enough elements"
    finally:
        print()
        return "Printed successfully"
