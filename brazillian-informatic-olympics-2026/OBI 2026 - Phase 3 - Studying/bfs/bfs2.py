from collections import deque
L, C = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(L)]
visitados = [[False] * C for _ in range(L)]
distancia = [[0] * C for _ in range(L)]
entrada_l, entrada_c, saida_l, saida_c = map(int, input().split())
direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(entrada_l, entrada_c):
    fila = deque([(entrada_l, entrada_c)])
    while fila:
        l, c = fila.popleft()
        visitados[l][c] = True
        if (l, c) == (saida_l, saida_c):
            return distancia[l][c]
        for dl, dc in direcoes:
            nl, nc = l + dl, c + dc
            if 0 <= nl < L and 0 <= nc < C:
                if visitados[nl][nc] == False and matriz[nl][nc] == 0:
                    fila.append((nl, nc))
                    distancia[nl][nc] = distancia[l][c] + 1
    return -1



print(bfs(entrada_l, entrada_c))

    #  0 1 2 3 4 5 6 7 
    #  ---------------
# l0 | 0 1 1 1 1 1 1 0
# l1 | 0 0 0 0 0 0 0 0
# l2 | 1 0 1 1 0 1 1 1
# l3 | 0 0 1 1 0 1 1 1
# l4 | 0 1 1 1 0 1 1 1
# l5 | 0 0 0 0 0 0 0 0
# l6 | 1 1 1 1 0 1 1 0
# l7 | 1 1 1 1 0 0 0 0

# fila = []
# l, c = 7, 4
# entrada = 0, 0
# saida = 7, 4
#Distancia
# 0 0 0 0 0 0 0 9
# 1 2 3 4 5 6 7 8
# 0 3 0 0 6 0 0 0
# 5 4 0 0 7 0 0 0
# 6 0 0 0 8 0 0 0
# 7 8 9 10 9 0 0 0
# 0 0 0 0 10 0 0 0
# 0 0 0 0 11 0 0 0
