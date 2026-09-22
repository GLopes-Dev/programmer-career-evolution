import heapq as hp

N, M = map(int, input().split())
grafo = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, peso = map(int, input().split())
    grafo[a].append((b, peso))
    grafo[b].append((a, peso))

dist = [float('inf')] * (N+1)
dist[1] = 0

fila = [(0, 1)]

while fila:
    d, u = hp.heappop(fila)
    if d > dist[u]:
        continue

    for vizinho, peso in grafo[u]:
        nova_distancia = d + peso

        if nova_distancia < dist[vizinho]:
            dist[vizinho] = nova_distancia
            hp.heappush(fila, (nova_distancia, vizinho))

print(dist[1:])

# grafo = [[], [(2, 4), (3, 2)], [(1, 4), (4, 3)], [(1, 3), (4, 1)], [(2, 3), (3, 1)]]
