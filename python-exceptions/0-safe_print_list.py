#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            try:
                if type(my_list[i]) is int:
                    print("{:d}".format(my_list[i]), end=" ")
                    count += 1
            except ValueError:
                pass
    except (IndexError, TypeError):
        pass
    finally:
        print()
        return count
