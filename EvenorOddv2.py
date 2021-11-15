#input
print('Even or Odd?')
num = input('Enter a whole number: ')

#processing
#output
if float(num) % 2 == 0:
    print('The number', num, 'is even.')
elif float(num) % 2 == 1:
    print('The number', num, 'is odd.')
else:
    print('The number you entered was not a whole number.')