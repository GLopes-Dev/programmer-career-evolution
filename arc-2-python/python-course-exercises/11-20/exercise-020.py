#Challenge 020 - The same teacher from the previous exercise wants to draw the order in which the student's work will be presented.
#Create a program that read the names of the 4 students and shows the randomly selected order on the screen
from random import shuffle
print('=' * 10, '[Challenge 020]', '=' * 10)
sList = []
for i in range(1, 5):
    names = input(f'{i}° Student Name: ')
    sList.append(names)
print('-' * 20)
shuffle(sList)
print(f'Order of Presentation:\n{sList}')
print('=' * 30)
 