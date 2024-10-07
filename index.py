"""
This file is intended for practice
purposes
"""

import sys

a = 1
b = 5
c = 10

# check if a is one
if a == 1:
  # print value of a
  print('a is', a)

print(a + b + c)

print(sys.version)

str_a = str(a)

print('This is a string a value', str_a)

float_a = float(a)

print('This is a float a value', float_a)

print('This is the type of float a value', type(float_a))

print('Is str_a really a string?', type(str_a) == str)

d, e, f = 'd', 'e', 'f'

print('Assignment to multiple variables', d, e, f)

collection = [1, 2, 3]

first_collection_value, second_collection_value, third_collection_value = collection

def function_working_with_global_variable():
  global third_collection_value
  third_collection_value = 'shadowed value (and also changed in the global scope)'
  print('Function called', first_collection_value, second_collection_value, third_collection_value)

function_working_with_global_variable()
print(third_collection_value)