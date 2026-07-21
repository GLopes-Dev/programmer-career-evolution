import sys
sys.setrecursionlimit(10**7)

#Variaveis [ 
L, C = map(int, sys.stdin.readline().split())
matriz = [list(map(int, sys.stdin.readline().split())) for _ in range(L)]
visitado = [[False] * C for _ in range(L)]
visitados = set()
#]

# Funcoes [
def dfs(x, y):
    visitado[x][y] = True
    direcoes = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1)
    ]
    for dl, dc in direcoes:
        nlinha = x + dl
        ncoluna = y + dc
        if 0 <= nlinha < L and 0 <= ncoluna < C:
            if not visitado[nlinha][ncoluna]:
                if matriz[nlinha][ncoluna] <= matriz[x][y]:
                    dfs(nlinha, ncoluna)
#]

# Codigo [
dfs(0, 0)
blocos = sum(linha.count(True) for linha in visitado)
print(blocos)
#