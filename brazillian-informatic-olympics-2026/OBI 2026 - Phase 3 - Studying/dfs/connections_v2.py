from collections import defaultdict
N, M = map(int, input().split())
conexoes = defaultdict(list)
visitados = set()
grupos = 0

def dfs(conexoes, visitados, x):
    visitados.add(x)
    for v in conexoes[x]:
        if v not in visitados:
            dfs(conexoes, visitados, v)

for _ in range(M):
    a, b = map(int, input().split())
    conexoes[a].append(b)
    conexoes[b].append(a)

for vertice in range(1, N+1):
    if vertice not in visitados:
        dfs(conexoes, visitados, vertice)
        grupos += 1

print(grupos)
