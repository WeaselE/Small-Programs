sel_num = input('Please enter a positive integer: ')
new_num = int(sel_num)

if int(new_num) <= 0:
    print('this number was negative.')
else:
    new_num = (((new_num * 2) * 5) / int(sel_num)) - 7
    print('Your number is now', str(int(new_num)) + '!')
