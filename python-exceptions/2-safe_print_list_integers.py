#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count_integers = 0
    try:
        for element in my_list[:x]:
            if type(element) == int:
                print("{:d}".format(element), end=' ')
                count_integers += 1
    except IndexError:
        pass
    finally:
        print()
    return count_integers
