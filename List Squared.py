def num_squared(num):
    return int(num ** 2)

lst = [int(i) for i in input("Enter numbers to square them (spaces between numbers): ").split()]
if lst:
    sqr_lst = [num_squared(i) for i in lst]
else:
    lst = range(11)
    sqr_lst = [num_squared(i) for i in lst]
print(sqr_lst)