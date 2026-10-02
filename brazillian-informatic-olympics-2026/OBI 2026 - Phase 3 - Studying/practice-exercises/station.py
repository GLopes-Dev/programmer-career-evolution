import heapq as hp

N, M = map(int, input().split())
matriz = []
passos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for l in range(N):
    linha = input().strip()
    matriz.append(linha)

    if 'S' in linha:
        l_inicio, c_inicio = l, linha.index('S')
    if 'E' in linha:
        l_final, c_final = l, linha.index('E')

distancia = [[float('inf')] * (M) for _ in range(N)]
distancia[l_inicio][c_inicio] = 0
fila = [(0, l_inicio, c_inicio)]

while fila:
    d, l, c = hp.heappop(fila)

    if d > distancia[l][c]:
            continue
    
    if matriz[l][c] == 'E':
        print(d)
        break

    for dl, dc in passos:
        nova_linha = dl + l
        nova_coluna = dc + c

        if 0 <= nova_linha < N and 0 <= nova_coluna < M:
            if matriz[nova_linha][nova_coluna] != '#':
                if matriz[nova_linha][nova_coluna] in ('E', 'S'):
                    nova_distancia = d + 0
                else:    
                    nova_distancia = d + int(matriz[nova_linha][nova_coluna])

                if nova_distancia < distancia[nova_linha][nova_coluna]:
                    distancia[nova_linha][nova_coluna] = nova_distancia
                    hp.heappush(fila, (nova_distancia, nova_linha, nova_coluna))

if distancia[l_final][c_final] == float('inf'):
    print(-1)
