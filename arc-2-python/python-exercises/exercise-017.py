#Challenge 017 - Make a program that reads the opposite side and adjacent side length of a right triangle, calculates and shows the hypotenuse length
from math import sqrt as rz
from math import pow
from math import hypot


#Without hypot() function

print('=' * 10, '[Challenge 017]', '=' * 10)
opS = float(input('Opposite side length: '))
adS = float(input('Adjacent side length: '))
print('-' * 35)
if opS <= 0 or adS <= 0:
    print("Geometrically impossible values to form a triangle, try again.")
else:
    print(f'The hypotenuse length is {rz(pow(opS, 2) + pow(adS, 2))}')
print('=' * 20)


#With hypot() function
print('=' * 10, '[Challenge 017]', '=' * 10)
opS = float(input('Opposite side length: '))
adS = float(input('Adjacent side length: '))
print('-' * 35)
if opS <= 0 or adS <= 0:
    print("Geometrically impossible values to form a triangle, try again.")
else:
    print(f'The hypotenuse length is {hypot(opS, adS)}')
print('=' * 20)


#Extra: added a if <=0 condition.