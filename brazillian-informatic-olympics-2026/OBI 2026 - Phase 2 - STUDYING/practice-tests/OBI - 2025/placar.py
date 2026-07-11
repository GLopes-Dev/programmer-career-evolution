import sys
P, *pMin = list(map(int, sys.stdin.readline().split()))
C, *cMin = list(map(int, sys.stdin.readline().split()))
gols = []
for min_gol in pMin:
    gols.append((min_gol, 'P'))
for min_gol in cMin:
    gols.append((min_gol, 'C'))
gols.sort()
Pg = 0
Cg = 0
print(f'{0} {0}')
for l in range(len(gols)):
    if 'C' in gols[l]:
        Cg += 1
        print(f'{Pg} {Cg}')
    elif 'P' in gols[l]:
        Pg += 1
        print(f'{Pg} {Cg}')
