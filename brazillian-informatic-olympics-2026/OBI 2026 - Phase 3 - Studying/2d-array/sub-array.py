N, M = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(N)]
vizinhos = [(0, 1), (1, 0), (1, 1)]
maior_soma = float("-inf")

def grid_sum(l, c):
    soma = matriz[l][c]
    for dl, dc in vizinhos:
        nova_linha = l + dl
        nova_coluna = c + dc
        if 0 <= nova_linha < N and 0 <= nova_coluna < M:
            soma += matriz[nova_linha][nova_coluna]
        else:
            soma = float("-inf")
            break

    return soma
for l in range(N):
    for c in range(M):
        maior_soma = max(maior_soma, grid_sum(l, c))

print(maior_soma)



