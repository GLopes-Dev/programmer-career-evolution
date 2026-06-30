import time
import random

elements = ['Rock', 'Paper', 'Scissors']
print('=' * 10, '[Challenge 045]', '=' * 10)
print('''Your options:
[ 0 ] ROCK
[ 1 ] PAPER
[ 2 ] SCISSORS''')
op = int(input("What's your move? "))
pc = random.choice(elements)
player = ''
win = None

match op:
    case 0:
        player = 'Rock'
        if pc == 'Scissors':
            win = True
        elif pc == 'Paper':
            win = False
    case 1:
        player = 'Paper'
        if pc == 'Rock':
            win = True
        elif pc == 'Scissors':
            win = False
    case 2:
        player = 'Scissors'
        if pc == 'Paper':
            win = True
        elif pc == 'Rock':
            win = False

print('-=' * 12)
print(f'''The Computer played {pc}
The Player played {player}''')
print('-=' * 12)

if win is True:
    print('PLAYER WINS')
elif win is False:
    print('COMPUTER WINS')
else:
    print('TIE!')
    