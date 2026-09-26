import heapq as hp

N, M = map(int, input().split())
grafo = [[] for _ in range(N+1)]
pai = [-1] * (N+1)

for _ in range(M):
    A, B, T = map(int, input().split())
    grafo[A].append((B, T))
    grafo[B].append((A, T))

temp = [float('inf')] * (N+1)
temp[1] = 0

fila = [(0, 1)]

while fila:
    tempo, cidade = hp.heappop(fila)
    if tempo > temp[cidade]:
        continue
    for vizinho, t in grafo[cidade]:
        nova_distancia = t + tempo

        if nova_distancia < temp[vizinho]:
            temp[vizinho] = nova_distancia
            hp.heappush(fila, (nova_distancia, vizinho))
            pai[vizinho] = cidade

if temp[N] == float('inf'):
    print(-1)
else:
    caminho = []
    atual = N

    while atual != -1:
        caminho.append(atual)
        atual = pai[atual]
        
    caminho.reverse()

    print(temp[N])
    print(*caminho)