#Challenge 016 - Make a program that reads a random Real number and shows nn the screen its integer portion.
#Ex: Type a number: 6.127
#The number 6.127 integer part is 6
from math import trunc

print('=' * 10, '[Challenge 016]', '=' * 10)
num = float(input('Type a number: '))
print(f'The number {num} integer part is {trunc(num)}\n', '=' * 35)