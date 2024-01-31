#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        result = None
    except Exception as e:
        print(f"Error: {e}")
        result = None
    finally:
        print("Inside result: {}".format(result))
