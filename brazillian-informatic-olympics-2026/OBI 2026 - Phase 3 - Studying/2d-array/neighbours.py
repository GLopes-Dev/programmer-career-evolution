N, M = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(N)]
matriz_copia = [[0] * M for _ in range(N)]
vizinhos = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def check(l, c):
    for dl, dc in vizinhos:
        nova_linha = l + dl
        nova_coluna = c + dc
        if 0 <= nova_linha < N and 0 <= nova_coluna < M:
            if matriz[nova_linha][nova_coluna] == 1:
                matriz_copia[l][c] += 1

for l in range(N):
    for c in range(M):
        check(l, c)


for linha in matriz_copia:
    print(*linha)