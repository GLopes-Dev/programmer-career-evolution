#Desafio 005 - Create a program that reads a INT number and shows in the screen its Sucessor and Predecessor
print('=' * 10,'[Challenge 005]', '=' * 10)
n = int(input('Type a number: '))
print('The {} sucessor is {}'.format(n, n+1))
print('The {} predecessor is {}'.format(n, n-1))
print('=' * 20)