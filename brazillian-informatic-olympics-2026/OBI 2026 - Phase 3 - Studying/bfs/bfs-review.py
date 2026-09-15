from collections import deque

N, M = map(int, input().split())
matriz = [list(input().strip()) for _ in range(N)]
distancia = [[-1] * M for _ in range(N)]
passos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
distancia[0][0] = 0

def bfs(x, y):
    fila = deque([(x, y)])
    while fila:
        l, c = fila.popleft()
        for dl, dc in passos:
            nova_linha = l + dl
            nova_coluna = c + dc
            if 0 <= nova_linha < N and 0 <= nova_coluna < M:
                if matriz[nova_linha][nova_coluna] == '.' and distancia[nova_linha][nova_coluna] < 0 :
                    fila.append((nova_linha, nova_coluna))
                    distancia[nova_linha][nova_coluna] = distancia[l][c] + 1

                if matriz[nova_linha][nova_coluna] == 'E':
                    distancia[nova_linha][nova_coluna] = distancia[l][c] + 1
                    return distancia[nova_linha][nova_coluna]
    return -1
print(bfs(0, 0))

