#Desafio 009 - Make a program that reads a random INT number and shows in the screen its multiplication table
print('=' * 10, '[Challenge 009]', '=' * 10)
num = int(input('Type a number: '))
print('-' * 30, '\n Multiplication Table')
for i in range (1, 11):
    print(f'{num} x {i} = {num * i}')
