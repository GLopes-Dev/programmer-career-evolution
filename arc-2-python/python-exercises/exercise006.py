#Desafio 006 - Create an algoritm that reads a number and show its double, its triple, and its Square Root
import math
print('=' * 10,'[Challenge 006]','=' * 10)
n = int(input('Type a number: '))
print(f'{n} double is {2 * n}')
print(f'{n} triple is {3 * n}')
print(f'{n} square root is {math.sqrt(n)}')
print('=' * 20)