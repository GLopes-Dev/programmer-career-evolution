#Desafio 013 - Make an algoritm that reads an employee salary and shows their new salary, with a 15% increase
from utilities import increase
print('=' * 10, '[Challenge 013]', '=' * 10)
incr = int(input('Increase: '))
salary = float(input('Salary: '))
final = increase(salary, incr)
print('-' * 35)
print(f'New salary: {final:.2f}\n', '=' * 35)
