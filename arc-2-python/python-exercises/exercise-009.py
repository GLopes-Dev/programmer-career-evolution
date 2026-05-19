#Desafio 009 - Make a program that reads a random INT number and shows in the screen its multiplication table
print('=' * 10, '[Challenge 009]', '=' * 10)
num = int(input('Type a number: '))
print('-' * 30, '\n Multiplication Table')
for i in range (1, 11):
    print(f'{num} x {i} = {num * i}')


#Learned how to use for loops and the range function to create a multiplication table for a given number. 
#The loop iterates from 1 to 10, multiplying the input number by the current value of i and printing the result in a formatted string.
#Learned it from TikTok