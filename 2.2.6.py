import math

x = int(input('Enter your x: '))
y = math.sin(x)
ep = float(input('Enter your epsilon: '))
row = x
n = 1

while math.fabs(y - row) > ep:
    n += 1
    row += math.pow(-1, n - 1) * math.pow(x, 2 * n - 1) / math.factorial(2 * n - 1)

print('when n =', n, 'row-y<ep')
print('value of function is', y)
print('value of row is', row)

input()