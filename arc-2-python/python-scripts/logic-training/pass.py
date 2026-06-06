import sys
import os

password = 1234
n = 3
print('=-' * 25)
for c in range(3):
    us_pass = int(input())
    if us_pass == password:
        print('Acess Granted.')
        sys.exit()
    else:
        n -= 1
        print(f'Wrong password, try again. ({n} attempts remaining.)')

os.system('cls' if os.name == 'nt' else 'clear')
print('=-' * 25)
print('Acess blocked.')