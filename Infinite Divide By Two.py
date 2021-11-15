from decimal import *
from time import sleep

def divide_by_two(nl):
    num = nl / 2
    return num

getcontext().prec = 100
n = Decimal(1.0)

while n != 0:
    n = divide_by_two(n)
    print(n)
    # sleep(0.025)
