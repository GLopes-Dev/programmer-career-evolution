import os

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Menu():
    print('=' * 50)
    print(' ' * 20, 'MAIN MENU', ' ' * 20)
    print('=' * 50)
    print(f'''{colors[1]}1 - {colors[2]} View registered Users
{colors[1]}2 - {colors[2]} Register new User
{colors[1]}3 - {colors[2]} Exit {colors[3]}''')
    print('=' * 50)

def Registered_Menu():
    print('=' * 50)
    print(' ' * 17, 'REGISTERED USERS', ' ' * 17)
    print('=' * 50)

colors = {1: '\033[;33m', 
          2: '\033[;34m', 
          3: '\033[;37m'}

#Main Code
Menu()
option = int(input(f'{colors[1]}Your Option: {colors[3]}'))
match option:
    case 1:
        Registered_Menu()
        with open(r'C:\Users\bielg\OneDrive\Documentos\Programmer Career Evolution\arc-2-python\python-course-exercises\111-120\exercise-120.txt', 'r') as arquivo:
            content = arquivo.read()
            print(content)