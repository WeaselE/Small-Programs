number = int(input(''))

while number > 0:
    print(int(number % 2), end='')
    number = int(number / 2)