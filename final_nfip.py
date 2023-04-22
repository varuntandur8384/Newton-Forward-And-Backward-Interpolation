n = int(input('Enter The Number Of Points: '))

import numpy as np
x = np.zeros((n))
y = np.zeros((n,n))

# calculating u 
def u_cal(u, n):
 
    temp = u
    for i in range(1, n):
        temp = temp * (u - i)
    return temp
 
# calculating factorial
def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

# reading X and Y value
print('Enter data for x: ')
for i in range(n):
    x[i] = float(input( 'enter the X value: '))

print('Enter data for y: ')
for i in range(n):
    y[i][0] = float(input('Enter The Y Value: '))
    
# Generating forward difference table
for i in range(1,n):
    for j in range(0,n-i):
        y[j][i] = y[j+1][i-1] - y[j][i-1]

        
print('\nFORWARD DIFFERENCE TABLE\n');

for i in range(0,n):
    print('%0.2f' %(x[i]), end='')
    for j in range(0, n-i):
        print('\t\t%0.2f' %(y[i][j]), end='')
    print()

value = float(input('Enter the interpolating value: '))


# initializing u and sum
sum = y[0][0]
u = (value - x[0]) / (x[1] - x[0])
for i in range(1,n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i)
 
#print("\nValue at", value,"is", round(sum, 6))
print("\nValue at", value,"is", sum )

