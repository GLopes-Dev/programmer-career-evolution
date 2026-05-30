#Challenge 032 - Create a program that reads a random year and display on the screen if it's a leap year.

print("=" * 10, "[Challenge 032]", "=" * 10)
year = int(input('Type a Year: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year. ")
else:
    print(f"{year} isn't a leap year. ")