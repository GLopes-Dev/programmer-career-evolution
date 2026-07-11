import sys

M, N = map(int, input().split())
matriz = []
for _ in range(M):
    matriz.append(list(input().split()))

direcoes = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

for l in range(M):
    for c in range(N):
        if matriz[l][c] == '*':
            continue
        bombas = 0
        for d_linha, d_coluna in direcoes:
            vizinho_l = l + d_linha
            vizinho_c = c + d_coluna
            if 0 <= vizinho_l < M and 0 <= vizinho_c < N:
                if matriz[vizinho_l][vizinho_c] == '*':
                    bombas += 1

        matriz[l][c] = str(bombas)

for linha in matriz:
    print(" ".join(linha))