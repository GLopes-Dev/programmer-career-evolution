print('=====[XP CALCULATOR]=====')
coins = int(input('Total Coins Amount: '))
time = int(input('Time: '))
print('-----------------------')
print('[1] Easy [2] Hard')
dificulty = int(input('Dificulty: '))
xp = (coins + time) * dificulty
bonus = xp * 1.5
print('=====[XP RESUME]=====')
print('Total XP amount: {}'.format(xp))
if (xp > 500):
    print('LEVEL UP!!!')
else:
    print('{} XP remain to level up'.format(500 - xp))
print('=====================')