from collections import defaultdict
N, M = map(int, input().split())
conexoes = defaultdict(list)
visitados = set()
grupos = 0
ordem = []

def dfs(conexoes, visitados, x):
    if x not in visitados:
        ordem.append(x)
        visitados.add(x)
    for v in conexoes[x]:
        if v not in visitados:
            dfs(conexoes, visitados, v)


for _ in range(M):
    a, b = map(int, input().split())
    conexoes[a].append(b)
    conexoes[b].append(a)

for x in conexoes:
    dfs(conexoes, visitados, x)
    if ordem:
        grupos += 1
        ordem = []
print(grupos)
