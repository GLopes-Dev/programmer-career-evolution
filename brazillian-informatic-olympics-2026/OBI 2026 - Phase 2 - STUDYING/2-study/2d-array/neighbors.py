

N, M = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(N)]
nova_matriz = [[0] * M for _ in range(N)]
direcoes = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1),
    (-1, -1), (-1, 1),
    (1, -1), (1, 1)
]
soma = 0
for l in range(N):
    for c in range(M):
        valor_atual = matriz[l][c]
        if valor_atual == 1:
            nova_matriz[l][c] = valor_atual
            continue

        for dl, dc in direcoes:
            nova_linha = l + dl
            nova_coluna = c + dc

            if 0 <= nova_linha < N and 0 <= nova_coluna < M:
                vizinho = matriz[nova_linha][nova_coluna]
                if vizinho == 1:
                    soma += 1
        nova_matriz[l][c] = soma
        soma = 0
print("-------")
for linha in nova_matriz:
    print(*linha)
                