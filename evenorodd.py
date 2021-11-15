import math

print('Is this number even?')
num = input('please enter a whole number: ')

if not (float(num)).is_integer():
    print('Error. Your number was not a whole number.')
elif int(num) % 2 == 0:
    print('True')
else:
    print('False')
