#Challenge 032 - Create a program that reads a random year and display on the screen if it's a leap year.
from datetime import date
print("=" * 10, "[Challenge 032]", "=" * 10)
year = int(input('Type a Year (Enter 0 to analyze the current year): '))
if year == 0:
    year = date.today().year

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year. ")
else:
    print(f"{year} isn't a leap year. ")
