#Challenge 011: Paint Calculator - Write a program that reads the width and height of a wall, calculates its area and the amount of paint needed to paint it,
#considering that 1 liter of paint covers 2 square meters.

print('=' * 10, '[Challenge 011]', '=' * 10)
width = float(input('Wall width: '))
height = float(input('Wall height: '))
area = width * height
print('-' * 30)
print(f"It's necessary at least {area / 2:.1f} liters of paint to paint a {area}m² area.")
print('=' * 30)