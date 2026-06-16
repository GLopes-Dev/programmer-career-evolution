# Challenge 039 - Create a program that reads a young man's birth year and, based on his age, 
# determines if he is yet to enlist for military service, if it's current time to enlist, 
# or if the enlistment deadline has already passed. 
# The program must also display the remaining time or the number of years overdue.


from datetime import date
import os

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Error():
    input('Wrong Option. Press ENTER to continue...')

birth_year = int(input('Birth Year: '))

while True:
    try:
        gender = input('Gender(Female/Male): ').upper()
        if gender[0] == 'F' or gender[0] == 'M':
            break
        else:
            Error()
            Clear()
            print(f'Birth Year: {birth_year}')
    except ValueError:
        Error()
        Clear()
        print(f'Birth Year: {birth_year}')
if gender[0] == 'F':
    print("You don't need to do the military enlistment, it's not mandatory for your gender.")
else:
    actual_year = date.today().year
    age = actual_year - birth_year

    print(f'Anyone born in {birth_year} would be {age} years old in {actual_year}.')

    if age < 18:
        print(f'There are still {18 - age} years until your military registration.')
        print(f'Your military enlisment will be in {actual_year + (18 - age)}')
    elif age == 18:
        print('You need to do your military enlistment IMMEDIATELY!')
    else:
        print(f'You were supposed to do your military enlistment {age - 18} years ago.')
        print(f'Your military enlistment was in {actual_year - (age - 18)}.')
