n1 = int(input('First number: '))
n2 = int(input('Second number: '))
s = n1 + n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
exp = n1 ** n2
mod = n1 % n2
print('The sum is {}\nThe division is {:.2f}\nThe product is {}\n'.format(s, d, m), end='')
print('The integer division is {}\nThe power is {}\nThe remainder of the division is {}\n'.format(di, exp, mod))