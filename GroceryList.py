grocery_list = []
item = input('Add an item to the grocery list: ')

while item:
    grocery_list.append(item)
    item = input('Add an item to the grocery list: ')

print('')
print('Your grocery list has', len(grocery_list), 'items.')
print(grocery_list)