#Challenge 041 - The National Swimming Confederation needs a program that reads an athlete's birth year and displays their category, based on their age:
#Up to 9 years old: Novice
#Up to 14 years old: Youth
#Up to 19 years old: Junior
#Up to 25 years old: Senior
#Above: Master

from datetime import date

print('=' * 10, '[Challenge 041]', '=' * 10)
birth_year = int(input('Birth Year: '))
current_year = date.today().year
age = current_year - birth_year
print(f'The Athlete is {age} years old.')
if age <= 9:
    print('Classification: Novice')
elif age <= 14:
    print('Classification: Youth')
elif age <= 19:
    print('Classification: Junior')
elif age <= 25:
    print('Classification: Senior')
else:
    print('Classification: Master')

