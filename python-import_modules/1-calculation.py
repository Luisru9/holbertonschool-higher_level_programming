#!usr/bin/python3
from calculator_1 import add, subtract, multiply, divide

a = 10
b = 5

result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)

print(f"Result of adding: {result_add}")
print(f"Result of subtracting: {result_subtract}")
print(f"Result of multiplying: {result_multiply}")
print(f"Result of dividing: {result_divide}")
