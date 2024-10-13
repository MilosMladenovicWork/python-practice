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

exec(open('print-hello-world.py', 'r').read())

with open('print-hello-world.py', 'r') as file:
  exec(file.read())

a = 'a'
b = 'b'
c = 'c'

print(a + b + c)

print('a' 'b' 'c')

print('a', 'b', "\"c\"", sep = "\n")

# name = input('Insert your name \n')
# age = int(input('Insert your age \n'))

# f_string = f'Your name is {name} and you are {age}'

# print(f_string)

q, w, e = 1, 2, 3

q = 10

print(q, w, e)

print('Sum', 2 + 3)
print('Difference', 5 - 3)
print('Multiplication', 2 * 7)
print('Division (float)', 8 / 4)
print('Division (int)', 9 // 2)
print('Modulo', 9 % 2)
print('Exponent', 2**4)
print('Exponent', 4**2)
print('=============')
print(123 + 456)
print(897.5 - 456.4)
print(345 * 789)
print(19 / 5)
print(725 * (14 + 18.2))
print(897 - (-456))
print((9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5))

rodjendan = int(input('How old are you? '))
godina = int(input('What is the year you celebrated birthday in? '))

print(f'You are born in year {godina - rodjendan}')

print(
  bool('Hello World!'),
  bool(10),
  bool(False),
  bool(None),
  bool(0),
  bool(""), 
  bool(-10)
)

# month_number = int(input('Insert month number: '))

# if month_number < 1 or month_number > 12:
#   print('You entered incorrect month number!')
# elif month_number >= 1 and month_number <= 3:
#   print('Month belongs in 1. quartal')
# elif month_number >= 4 and month_number <= 6:
#   print('Month belongs in 2. quartal')
# elif month_number >= 7  and month_number <= 9:
#   print('Month belongs in 3. quartal')
# else:
#   print('Month belongs in 4. quartal')

number_of_seconds = int(input('Insert number of seconds: '))

number_of_seconds_in_minute = 60
number_of_seconds_in_hour = 3600
number_of_seconds_in_day = 86400

days = number_of_seconds // number_of_seconds_in_day
hours = (number_of_seconds - days * number_of_seconds_in_day) // number_of_seconds_in_hour
minutes = (number_of_seconds - days * number_of_seconds_in_day - hours * number_of_seconds_in_hour) // number_of_seconds_in_minute
seconds = number_of_seconds - days * number_of_seconds_in_day - hours * number_of_seconds_in_hour - minutes * number_of_seconds_in_minute

if number_of_seconds >= number_of_seconds_in_day:
  print(f'{days} days, {hours} hours, {minutes} minutes and {seconds} seconds')
elif number_of_seconds >= number_of_seconds_in_hour:
  print(f'{hours} hours and {minutes} minutes and {seconds} seconds')
elif number_of_seconds >= number_of_seconds_in_minute:
  print(f'{minutes} minutes and {seconds} seconds')

