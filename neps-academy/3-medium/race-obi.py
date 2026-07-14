import sys
N, M = map(int, sys.stdin.readline().split())
ranking = []
for c in range(N):
    tempo = list(map(int, sys.stdin.readline().split()))
    tempo_total = sum(tempo)
    competidor = c + 1
    ranking.append((tempo_total, competidor))
ranking.sort()
print(ranking[0][1])

    