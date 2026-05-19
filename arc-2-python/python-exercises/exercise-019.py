#Challenge 019 - A teacher wants to draw one of your students to erase the board. Make a program that helps him, reading the name of each students and showing the selected student
#name.

from random import choice

#Normal version

print('=' * 10, '[Challenge 019]', '=' * 10)
s1 = input('First Student: ')
s2 = input('Second Student: ')
s3 = input('Third Student: ')
s4 = input('Fourth Student: ')
students = [s1, s2, s3, s4]
print('-' * 20)
print(f'The student drawn is {choice(students)}\n', '=' * 20)


#Loop version

print('=' * 10, '[Challenge 019]', '=' * 10)
sList = []
for i in range(1, 5):
    student = input(f'{i} Student: ')
    sList.append(student)
print('-' * 20)
print(f'The student drawn is {choice(sList)}\n', '=' * 20)