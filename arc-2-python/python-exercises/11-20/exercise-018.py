#Challenge 018 - Make a program that reads a random angle and shows in the screen the sine value, cosine value and tangent value of that angle

from math import sin, cos, tan, radians

print('=' * 10, '[Challenge 018]', '=' * 10)
angle = float(input('Type an angle: '))
print('-' * 35)
print(f'{angle}° Sine is {sin(radians(angle)):.2f}.\n{angle}° Cosine is {cos(radians(angle)):.2f}.\n{angle}° Tangent is {tan(radians(angle)):.2f}.')
print('=' * 20)