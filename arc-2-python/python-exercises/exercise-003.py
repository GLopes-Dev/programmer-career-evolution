#Desafio 003 - Create a program that read both numbers and show the SUM between then

print('=========[Challenge 003]=========')
n1 = int(input('Type the first number: '))
n2 = int(input('Type the second number: '))
s = n1 + n2
med = s / 2
mult = n1 * n2
div = n1 / n2
exp = n1 ** n2
print('The sum between {} and {} is: {}'.format(n1, n2, s))
print('The average between {} and {} is: {}'.format(n1, n2, med))
print('The multiplication between {} and {} is: {}'.format(n1, n2, mult))
print('The division between {} and {} is: {}'.format(n1, n2, div))
print('The exponentiation between {} and {} is: {}'.format(n1, n2, exp))