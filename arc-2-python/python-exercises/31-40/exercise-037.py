#Challenge 037 - Create a program that reads any Integer and then asks the User to choose the conversion base:
# - 1 for Binary
# - 2 for Octal
# - 3 for Hexadecimal

#OBS: Did an error treatment system in this one using all my knowledge that I have in this topic

import os

def screen_menu():
    print('Choose one of the bases for conversion: ')
    print('[ 1 ] Convert to Binary\n[ 2 ] Convert to Octal\n[ 3 ] Convert to Hexadecimal')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        N = int(input('Type an integer: '))
        break
    except ValueError:
        print('Type only Integer Numbers.')
        input('ENTER to continue...')
        clear_screen()


while True:
    screen_menu()
    try:
        option = int(input('Your option: '))
        if 1 <= option <= 3:
            break
        else:
            print(f'Invalid Option. Try again. \n')
            input('ENTER to continue...')
            clear_screen()
            print(f'Your Integer: {N}\n')
    except ValueError:
        print('Type only Integer Numbers.')
        input('ENTER to continue...')
        clear_screen()
        print(f'Your Integer: {N}\n')

if option == 1:
    print(f'{N} converted to BINARY equals {bin(N)[2:]}')
elif option == 2:
    print(f'{N} converted to OCTAL equals {oct(N)[2:]}')
else:
    print(f'{N} converted to HEXADECIMAL equals {hex(N)[2:]}')