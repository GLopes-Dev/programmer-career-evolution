import sys
N, M = map(int, sys.stdin.readline().split())
ranking = []
for c in range(N):
    tempos = list(map(int, sys.stdin.readline().split()))
    tempo_total = sum(tempos)
    numero_carro = c + 1
    ranking.append((tempo_total, numero_carro))
ranking.sort()
for c in range(3):
    print(f'{ranking[c][1]}')
