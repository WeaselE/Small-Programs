mango_price = 1.25
print('Mangoes are', '$' + str(mango_price), 'each day.')
mango_count = int(input('How many mangoes would you like to buy: '))

mango_total = '{:.2f}'.format(mango_price * mango_count)

print('That will be', '$' + str(mango_total), 'please')
