#Challenge 014 - Make a program that converts a temperature typed in Celsius and converts it to Fahrenheit
from utilities import celsius_to_fahrenheit
print('=' * 10, '[Challenge 014]', '=' * 10)
celsius = float(input('Temperature in Celsius: '))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius:.1f}°C converted to °F is {fahrenheit:.1f}°F.")
print('=' * 35)


#Learned importing functions from other files, and how to use them. Learned it from tiktok