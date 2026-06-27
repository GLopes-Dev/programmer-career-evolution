N = int(input())
competidores = {}
for c in range(N):
    competidor, ponto = input().split()
    ponto = int(ponto)
    competidores[competidor] = ponto

ranking = sorted(competidores.items(), key=lambda x: (-x[1], x[0]))
for c, p in ranking:
    print(f"{c}: {p}")