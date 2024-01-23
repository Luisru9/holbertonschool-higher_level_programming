#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#Code to give the information about + or - number
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")