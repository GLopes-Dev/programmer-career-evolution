#Just for tests



from random import random

print('=' * 10, '[Challenge 019]', '=' * 10)
s1 = input('First Student: ')
s2 = input('Second Student: ')
s3 = input('Third Student: ')
s4 = input('Fourt Student: ')
print('-' * 20)
print(f'The student drawn is {random(s1, s2, s3, s4)}\n', '=' * 20)