from os import system



i = input("Min Number: ")
i = int(i)

n = input("Max Number: ")
n = int(n)

lst = []

system('cls')

while (i <= n):
    lst.append(i)
    i = i + 1
print(lst)
input("")