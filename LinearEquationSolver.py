''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

#define variables
x = 0
y = 0
b_temp = b
c_temp = c
e_temp = e
f_temp = f

#make equations have equal number of x

e_temp *= a
f_temp *= a
b_temp *= -d
c_temp *= -d

#Combine equations

b_temp += e_temp
c_temp += f_temp

#find y

y = c_temp / b_temp

#Use y to find x

c -= (b * y)
x = c / a

print(int(x), int(y))