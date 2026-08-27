from collections import deque
N = int(input())
amizades = {}
for p in range(N):
    A, B = input().split()
    amizades.setdefault(A, []).append(B)
    amizades.setdefault(B, []).append(A)
origem = input()
destino = input()
visitados = set()
distancia = {origem: 0}
def bfs(origem, destino, amizades, visitados):
    fila = deque([origem])
    while fila:
        atual = fila.popleft()
        if atual == destino:
            return distancia[atual]
        for v in amizades.get(atual, []):
            if v not in distancia:
                fila.append(v)
                distancia[v] = distancia[atual] + 1

    return -1

print(bfs(origem, destino, amizades, visitados))


