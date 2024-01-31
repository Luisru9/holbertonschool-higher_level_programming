#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    count_elements = 0
    try:
        for i in range(x):
            # Replace the print statement with an empty string
            result_str = "{} ".format(my_list[i])
            count_elements += 1
    except IndexError:
        pass
    finally:
        # Print the result string outside the loop
        print(result_str)
    return count_elements
