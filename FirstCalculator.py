x = int(input('Please input the first number: '))
y = int(input('Please input the second number: '))
operator = input('Please enter an operator (+, -, *, /, or ^): ')
ans = 0

#define operators
def plus(x, y):
    return x + y
def minus(x, y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    return x / y
def power(x,y):
    return x ** y

#process input, direct to proper function
if operator == '+':
    print(plus(x,y))
elif operator == '-':
    print(minus(x,y))
elif operator == '*':
    print(multiplication(x,y))
elif operator == '/':
    print(division(x,y))
elif operator == '^':
    print(power(x,y))