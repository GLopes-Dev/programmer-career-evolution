import sys
sys.setrecursionlimit(200000)

N, M = map(int, input().split())
matriz = [list(input().strip()) for i in range(N)]
visitados = [[False] * M for i in range(N)]
passos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
regioes = 0

def dfs(x, y):
    visitados[x][y] = True
    for dl, dc in passos:
        nl = x + dl
        nc = y + dc
        if 0 <= nl < N and 0 <= nc < M:
            if matriz[nl][nc] == '#' and visitados[nl][nc] == False:
                dfs(nl, nc)

for l in range(N):
    for c in range(M):
        if not visitados[l][c] and matriz[l][c] == '#':
            dfs(l, c)
            regioes += 1

print(regioes)