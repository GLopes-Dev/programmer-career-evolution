from collections import deque
L, C = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(L)]
visitados = [[False] * C for _ in range(L)]
entrada_l, entrada_c, saida_l, saida_c = map(int, input().split())
direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
distancia = 0
def bfs(entrada_l, entrada_c):
    global distancia
    fila = deque([(entrada_l, entrada_c)])
    while fila:
        l, c = fila.popleft()
        visitados[l][c] = True
        if (l, c) == (saida_l, saida_c):
            return distancia
        distancia += 1
        for dl, dc in direcoes:
            nl, nc = l + dl, c + dc
            if 0 <= nl < L and 0 <= nc < C:
                if visitados[nl][nc] == False and matriz[nl][nc] == 0:
                    fila.append((nl, nc))
    return -1

print(bfs(entrada_l, entrada_c))

# 0 0 0
# 1 1 0 
# 0 0 0
# distancia = 1
# fila = [(0, 1)]
# l, c = (0, 0)
# entrada = (0, 0)
# saida = (2, 2)